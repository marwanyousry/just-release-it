#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[33m'
NC='\033[0m' # No Color
# set global variables for build
IS_PROD=true # indicate if we want to release a production build or not
NEW_VERSION_CODE=20041 # incase we release a production build this is the new version code 
NEW_VERSION_NAME='2.0.41' # incase we release a production build this is the new version name 

# this function print in termainal a message ex: println "message"
println() {
    local message="$1"
    echo -e "${GREEN}${message}${NC}"
}

navToScripts() {
    cd ./builds/scripts
}
navToRoot() {
    local num=$1
    for ((i = 0; i < num; i++)); do
        cd ..
    done
}
navToAndroid() {
    cd ./android
}
navToiOS() {
    cd ./ios/app
}