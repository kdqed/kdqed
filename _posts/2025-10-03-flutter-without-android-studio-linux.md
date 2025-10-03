---
cover_image: confused-android.webp
title: "Setup Flutter & Android SDK Without Android Studio On Linux"
permalink: flutter-without-android-studio-linux
---

Android Studio is such a resource hog! Plus, I'm not a fan of IDEs, I like a minimal editor (check out [Lite XL](https://lite-xl.com/)) and prefer to use the command line as much as I can. Setting up Android SDK and Flutter without Android Studio has always been a pain and not much documentation is provided by Google in this regard. So I'm documenting the latest process I followed in this blog.

I'm currently on a Debian 13 system, and I typically use Flutter to make Android apps. I don't run emulators, I rather test the app as a Linux dekstop app, and finally build for the Android platform. This makes the whole process resource efficient, and increases my iteration speed. So the instructions below will have you set up for building Linux and Android apps with Flutter.
> **NOTE:** This works as of October 2025

## 1. For Linux Desktop

### 1.1. Install Basic Dependencies

Get the dependecies from the [Flutter docs](https://docs.flutter.dev/install/manual) and install them

```bash
$ sudo apt install curl git unzip xz-utils zip libglu1-mesa
$ sudo apt install clang cmake ninja-build pkg-config libgtk-3-dev liblzma-dev libstdc++-12-dev
```

### 1.2. Install Mesa Utils, Ensure `glxinfo` And `glxgears` Are Working

Necessary if you're using a barebones window manager like i3 or Openbox (like I do).

```bash
$ sudo apt install mesa-utils

$ glxinfo -B
name of display: :0
display: :0  screen: 0
direct rendering: Yes
Extended renderer info (GLX_MESA_query_renderer):
    Vendor: Intel (0x8086)
    Device: Mesa Intel(R) HD Graphics 4400 (HSW GT2) (0xa16)

$ glxgears
// should show a window with 3 rotating gears in red, green, and blue colors.
```

## 2. Install Flutter SDK

Check the latest version on the Flutter site and run the following to install Flutter:

```bash
$ export LATEST_FLUTTER_VERSION=3.35.5-stable
$ wget "https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_${LATEST_FLUTTER_VERSION}.tar.xz"
$ tar -xvf "flutter_linux_${LATEST_FLUTTER_VERSION}.tar.xz"
$ mv flutter ~/.flutter-sdk
$ echo 'export PATH=$HOME/.flutter-sdk/bin:$PATH' >> ~/.bashrc
$ source ~/.bashrc
$ rm "flutter_linux_${LATEST_FLUTTER_VERSION}.tar.xz"
```

Ensure it's installed and added to PATH:

```bash
$ flutter doctor -v
[✓] Flutter (Channel stable, 3.35.5, on Debian GNU/Linux 13 (trixie) 6.12.48+deb13-amd64, locale en_IN) [48ms]
    • Flutter version 3.35.5 on channel stable at /home/kd/.flutter-sdk
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision ac4e799d23 (6 days ago), 2025-09-26 12:05:09 -0700
    • Engine revision d3d45dcf25
    • Dart version 3.9.2
    • DevTools version 2.48.0
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop, enable-android, enable-ios, cli-animations, enable-lldb-debugging
...
[✓] Linux toolchain - develop for Linux desktop [1,035ms]
    • Debian clang version 19.1.7 (3+b1)
    • cmake version 3.31.6
    • ninja version 1.13.0.git.kitware.jobserver-pipe-1
    • pkg-config version 1.8.1
    • OpenGL core renderer: Mesa Intel(R) HD Graphics 4400 (HSW GT2) (X11)
    • OpenGL core version: 4.6 (Core Profile) Mesa 25.0.7-2 (X11)
    • OpenGL core shading language version: 4.60 (X11)
    • OpenGL ES renderer: Mesa Intel(R) HD Graphics 4400 (HSW GT2) (X11)
    • OpenGL ES version: OpenGL ES 3.2 Mesa 25.0.7-2 (X11)
    • OpenGL ES shading language version: OpenGL ES GLSL ES 3.20 (X11)
    • GL_EXT_framebuffer_blit: yes (X11)
    • GL_EXT_texture_format_BGRA8888: yes (X11)
```

## 3. Test Linux App

Run the example app on Linux and make sure you see it running:

```bash
$ flutter create linux_test_app
$ cd linux_test_app
$ flutter run
// Sample App Runs

$ cd ..
$ rm -rf linux_test_app
```

## 4. Download And Setup Android SDK

### 4.1. Install Java Dependencies

```bash
$ sudo apt install openjdk-17-jdk openjdk-17-jre
```

### 4.2. Download And Setup Android SDK Command Line Tools

Replace XXXXXXXX with the identifier from the Studio webpage's Command Line Tools section: [https://developer.android.com/studio#command-tools](https://developer.android.com/studio#command-tools)

```bash
$ wget https://dl.google.com/android/repository/commandlinetools-linux-XXXXXXXX_latest.zip
$ unzip commandlinetools-linux-XXXXXXXX_latest.zip -d ~/.android-sdk
$ rm commandlinetools-linux-XXXXXXXX_latest.zip
```

It's necessary to move some things around:

```bash
$ cd ~/.android-sdk
$ mv cmdline-tools latest
$ mkdir cmdline-tools
$ mv latest cmdline-tools/ 
```

Add some variables to `~/.bashrc`

```bash
$ echo 'export ANDROID_HOME=$HOME/.android-sdk' >> ~/.bashrc
$ echo 'export ANDROID_USER_HOME=$HOME/.android' >> ~/.bashrc
$ echo 'export PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$PATH' >> ~/.bashrc
$ source ~/.bashrc
```

### 4.3. Install & Setup Build Tools

Get latest required version from [https://docs.flutter.dev/platform-integration/android/setup](https://docs.flutter.dev/platform-integration/android/setup). Then get the exact version code using `sdkmanager`:

```bash
$ sdkmanager --list | grep 'build-tools.*36'
build-tools;36.0.0      | 36.0.0      | Android SDK Build-Tools 36                                            
build-tools;36.0.0-rc1  | 36.0.0 rc1  | Android SDK Build-Tools 36-rc1                                        
build-tools;36.0.0-rc3  | 36.0.0 rc3  | Android SDK Build-Tools 36-rc3                                        
build-tools;36.0.0-rc4  | 36.0.0 rc4  | Android SDK Build-Tools 36-rc4                                        
build-tools;36.0.0-rc5  | 36.0.0 rc5  | Android SDK Build-Tools 36-rc5                                        
build-tools;36.1.0      | 36.1.0      | Android SDK Build-Tools 36.1                                          
build-tools;36.1.0-rc1  | 36.1.0 rc1  | Android SDK Build-Tools 36.1-rc1 
```

I'd say install the latest version that is not an `rc`.

```bash
$ sdkmanager --install 'build-tools;36.1.0'
$ echo 'export PATH=$ANDROID_HOME/build-tools/36.1.0:$PATH' >> ~/.bashrc
$ source ~/.bashrc
```

### 4.4. Install & Setup Platform Tools

```bash
$ sdkmanager --install platform-tools
$ echo 'export PATH=$ANDROID_HOME/platform-tools:$PATH' >> ~/.bashrc
$ source ~/.bashrc
```

### 4.5. Install A Platform

Get latest recommended version from [https://docs.flutter.dev/platform-integration/android/setup](https://docs.flutter.dev/platform-integration/android/setup)

```bash
$ sdkmanager --install 'platforms;android-36'
```

### 4.6. Accept Licenses

```bash
$ flutter doctor --android-licenses
```

### 4.7. Run Flutter Doctor

```bash
$ flutter doctor -v
...
[✓] Android toolchain - develop for Android devices (Android SDK version 36.1.0) [3.1s]
    • Android SDK at /home/kd/.android-sdk
    • Emulator version unknown
    • Platform android-36, build-tools 36.1.0
    • ANDROID_HOME = /home/kd/.android-sdk
    • Java binary at: /usr/bin/java
      This JDK was found in the system PATH.
      To manually set the JDK path, use: `flutter config --jdk-dir="path/to/jdk"`.
    • Java version OpenJDK Runtime Environment (build 17.0.17-ea+8-Debian-1)
    • All Android licenses accepted.
...
```

### 4.8. Some Gradle Shenanigans
The first `flutter run` after connecting an Android device will take almost 30 minutes; for downloading Gradle and other Java stuff. To see what's happening, run it in verbose mode:

```bash
flutter run -v
```

## 5. Conclusion

Hopefully everything worked as expected! I will try to keep updating this guide everytime I have to setup afresh.
