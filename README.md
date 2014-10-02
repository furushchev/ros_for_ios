ros-ios
===========

## How to build

1. build ros core for iOS

```
sh build.sh
```

2. create your xcode project

Open xcode, create your own project, then save it to this top directory.

After creating the project named `hogeApp`, directory tree is like below:

```
/path/to/ros-ios/
 |- new-app.sh
 |- hogeApp/
 |     |- hogeApp.xcodeproj
 |     ...
 |- ros/
```

3. apply ros to your project

```
sh new-app.sh
```

4. Have a fun!

You can build your app at xcode.

## How to generate own ros package to framework

```
cd /path/to/ros-ios/ros
sh message_gen.sh -f /path/to/hoge_msgs /path/to/depend1_msgs /path/to/depend2_msgs ...
```

This will build `hoge_msgs.framework` which depends of `depend1_msgs` and `depend2_msgs` (it's also 
possible to generate a simple folder with the -d option instead of the -f).

iOS demo applications
---------------------

It's an Xcode project which can be found in the xcode_project directory.
