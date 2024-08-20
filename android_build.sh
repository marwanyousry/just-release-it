#!/bin/bash
source shared.sh # import all functions in shared shell file 
sync_android() {
    rm -rf builds/android/app-release.apk
    println ">>>> start building android folder"
    ionic build 
    ionic capacitor sync android 
    println ">>>> start apply androidX fixes"
    npx jetify
    ionic capacitor sync android 
    println ">>>> android build process completed"
}
android_platform_fixes() {
    println ">>>> running python script to fix android files"
    navToScripts
    python3 fix-android-capacitor-manifest.py
    python3 fix-andorid-node-modules.py
    navToRoot 2
    println ">>>> python fixes applied successfully"
}
android_release_build() {
    navToAndroid
    println ">>>> start clean andorid project"
    ./gradlew clean
    println ">>>> start generating build"
    if [ "$1" = true ]; then
        PnewVersionName=$3
        PnewVersionCode=$2
    else
        PnewVersionName=$(python3 -c "from pygit2 import Repository; print(Repository('.').head.shorthand.split('/')[1].split('-')[0])")
        PnewVersionCode=$(python3 -c "from datetime import datetime; print(datetime.today().strftime('%y%m%d'))")
    fi
    ./gradlew assembleRelease -PnewVersionCode=$PnewVersionCode -PnewVersionName=$PnewVersionName
    println ">>>> android bundle created successfully"
    navToRoot 1
    navToScripts
    python3 copy-android-release.py
    navToRoot 2
}
upload_android_release(){
    println ">>>> start uploading android release "
    navToScripts
    python3 app-center-android.py
    python3 show-notification.py Android
    println ">>>> android bundle uploaded to appCenter successfully"
    navToRoot 2
}



# sync_android
# android_platform_fixes
# android_release_build $IS_PROD $NEW_VERSION_CODE "$NEW_VERSION_NAME"
# upload_nadroid_release

