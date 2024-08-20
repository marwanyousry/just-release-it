import appcenter
import platform
from config import config
# access_token created from AppCenter Dashboard for only iOS app FullAccess 
# group_id from settings for each group there is an identifier under it's name 
# both owner name and app name could be noticed from application url  owner name is the name after users/ and app_name the path after apps/
platform_config = config['ios']
release_note = 'iOS Build Uploaded using python script by ' + platform.node() + ' machine'
client = appcenter.AppCenterClient(access_token=platform_config["access_token"])

release = client.versions.upload_and_release(
    owner_name=platform_config["owner_name"],
    app_name=platform_config["app_name"],
    binary_path=platform_config["binary_path"],
    group_id=platform_config["group_id"],
    release_notes=release_note,
    notify_testers=True
)
# append to email txt file iOS build link 
release_url = f"https://install.appcenter.ms/users/{platform_config['owner_name']}/apps/{platform_config['app_name'].lower()}/distribution_groups/public/releases/{release.identifier}"
with open("./../email.txt", "a") as file:
    file.write(f'\n\niOS : {release_url}\n')
    file.write(f'iOS : https://install.appcenter.ms/users/{platform_config["owner_name"]}/apps/{platform_config["app_name"]}/releases/{release.identifier}\n')
