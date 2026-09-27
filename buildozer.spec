[app]

title = StrikeCore
package.name = strikecore
package.domain = org.strikecore
source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,wav,ogg,json,txt,md
source.exclude_dirs = .git,.github,.buildozer,bin,__pycache__
version = 0.1
requirements = python3,kivy,pillow,numpy
orientation = landscape
fullscreen = 1
android.api = 35
android.minapi = 23
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE
