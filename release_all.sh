#!/bin/bash
source shared.sh # import all functions in shared shell file
source android_build.sh # import all functions in android_build shell file
source ios_build.sh # import all functions in ios_build shell file
#!/bin/bash
set -e  # Stop the script if any command fails
println "***********************************************************************"

sync_android
android_platform_fixes
android_release_build $IS_PROD $NEW_VERSION_CODE "$NEW_VERSION_NAME"
upload_android_release

println "***********************************************************************"

sync_ios
update_xcode_settings
build_ios $IS_PROD
upload_ios_release