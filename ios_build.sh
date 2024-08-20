#!/bin/bash
source shared.sh # import all functions in shared shell file
sync_ios() {
    rm -rf builds/ios/App.ipa
    println ">>>> start build ios folder"
    ionic build 
    ionic capacitor sync ios 
    println ">>>> ios changes synced successfully"
}

update_xcode_settings() {
    println ">>>> update xcode version and signing options"
    navToScripts
    python3 update-xcode-info.py "$IS_PROD" "$NEW_VERSION_CODE" "$NEW_VERSION_NAME"
    python3 updateSwift.py
    navToRoot 2
}

build_ios() {
    navToiOS
    println ">>>> start cleaning xcode project"
    xcodebuild clean -workspace App.xcworkspace -scheme AppRelease 
    println ">>>> start building xcode project"
    xcodebuild build -workspace App.xcworkspace -scheme AppRelease 
    navToRoot 2
    navToScripts
    python3 fix-ios-config.py
    python3 fix-pod-shell.py
    navToRoot 2
    navToiOS
    println ">>>> start archiving xcode project"
    xcodebuild archive -workspace App.xcworkspace -scheme AppRelease -archivePath ./../../archive/App.xcarchive 

    println ">>>> start exportinig new iOS release"
    if [ "$1" = true ]; then
        xcodebuild -exportArchive -archivePath ./../../archive/App.xcarchive -exportPath ./../../builds/ios -exportOptionsPlist ./../../builds/ios/ExportOptionsStore.plist 
    else
        xcodebuild -exportArchive -archivePath ./../../archive/App.xcarchive -exportPath ./../../builds/ios -exportOptionsPlist ./../../builds/ios/ExportOptionsEnt.plist 
    fi
    navToRoot 2
    rm -rf ./archive
}

upload_ios_release() {
    println ">>>> start uploading iOS release to appCenter"
    navToScripts
    python3 app-center-ios.py
    python3 show-notification.py iOS
    navToRoot 2
}

# sync_ios
# update_xcode_settings
# build_ios $IS_PROD
# upload_ios_release