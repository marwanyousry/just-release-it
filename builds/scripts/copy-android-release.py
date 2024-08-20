import shutil
# copy the generated APK file to outside the android platform folder to be used in uploading release to appCenter 
shutil.copy2('./../../android/app/build/outputs/apk/release/app-release.apk', './../android/app-release.apk')
