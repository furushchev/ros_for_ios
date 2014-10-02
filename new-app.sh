#!/bin/bash

SRCDIR=`pwd`

###

if [ ! -d $SRCDIR/mod_pbxproj ]; then
    git submodule init
    git submodule update
fi

echo "Welcome to ROS-iOS App Generator!"
read -p "What is your app name? (ros-ios-app): " APPNAME
APPNAME=${APPNAME:-"ros-ios-app"}

###

echo "Checking the directory..."
PBXPROJ="$SRCDIR/$APPNAME/$APPNAME.xcodeproj/project.pbxproj"
APPLIEDP="$SRCDIR/$APPNAME/.ROS_APPLIED"
if [ -e $PBXPROJ ]; then
    if [ -e $APPLIEDP ]; then
        echo "ROS Packages are already added to your project"
        echo "Aborting..."
        exit 1
    else
        python add-ros-framework-to-xcodeproj.py $APPNAME
        touch $APPLIEDP
    fi
else
    echo "No Xcode Project found."
    echo "Is there $APPNAME.xcodeproj in $SRCDIR/$APPNAME directory?"
    echo "Aborting..."
    exit 1
fi

echo "OK!"
