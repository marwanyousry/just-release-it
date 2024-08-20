import fileinput
import sys
from pygit2 import Repository
from datetime import date
import arrow
import os
from config import xCodeConfig 
# there is agv tool Apple Generic Version tool is used to update xCode project version name and build number but now there is an issue in updating version name with xCode 14.3
# as a work around we will update them in 2 steps 
# this script should be executed after build ios capacitor folder and before clean xCode workspace 

today = str(date.today())
strToday = arrow.get(today, 'YYYY-MM-DD')
# build number contains today formatted YYMMDD ex : 230517
dateFormatted = strToday.format('YYMMDD')

# Extract parameters from command line arguments
is_prod = sys.argv[1]
production_version_code = sys.argv[2]
production_version_name = sys.argv[3]

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=True):
        if searchExp in line:
            line = '                '+replaceExp+';'+'\n'
        sys.stdout.write(line)
branchCode = Repository('.').head.shorthand.split('/')[1].split('-')[0]

if is_prod.lower() == 'true':
    version_number = production_version_name
    build_number = production_version_code
    platform_config = xCodeConfig['store']
else:
    version_number = branchCode
    build_number = dateFormatted
    platform_config = xCodeConfig['enterprise']


# Update project settings based on the configuration
replaceAll('./../../ios/App/App.xcodeproj/project.pbxproj', 'CODE_SIGN_IDENTITY', f'CODE_SIGN_IDENTITY = "{platform_config["CODE_SIGN_IDENTITY"]}"')
replaceAll('./../../ios/App/App.xcodeproj/project.pbxproj', '"CODE_SIGN_IDENTITY[sdk=iphoneos*]"', f'"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "{platform_config['"CODE_SIGN_IDENTITY[sdk=iphoneos*]"']}"')
replaceAll('./../../ios/App/App.xcodeproj/project.pbxproj', '"DEVELOPMENT_TEAM[sdk=iphoneos*]"', f'"DEVELOPMENT_TEAM[sdk=iphoneos*]" = {platform_config["DEVELOPMENT_TEAM"]}')
replaceAll('./../../ios/App/App.xcodeproj/project.pbxproj', 'PRODUCT_BUNDLE_IDENTIFIER', f'PRODUCT_BUNDLE_IDENTIFIER = {platform_config["PRODUCT_BUNDLE_IDENTIFIER"]}')
replaceAll('./../../ios/App/App.xcodeproj/project.pbxproj', '"PROVISIONING_PROFILE_SPECIFIER[sdk=iphoneos*]"', f'"PROVISIONING_PROFILE_SPECIFIER[sdk=iphoneos*]" = {platform_config["PROVISIONING_PROFILE_SPECIFIER"]}')

# Update version and build number
replaceAll('./../../ios/App/App.xcodeproj/project.pbxproj', 'MARKETING_VERSION', 'MARKETING_VERSION = '+ version_number)
replaceAll('./../../ios/App/App.xcodeproj/project.pbxproj', 'CURRENT_PROJECT_VERSION', 'CURRENT_PROJECT_VERSION = '+ build_number) # date

### second step will execute terminal commands from python using os.system and plutil to update Info.plist file 
os.system('plutil -replace CFBundleShortVersionString -string '+ version_number +' ./../../ios/App/App/Info.plist')
os.system('plutil -replace CFBundleVersion -string '+ build_number +' ./../../ios/App/App/Info.plist')
