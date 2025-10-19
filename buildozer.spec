[app]
title = Voice Assistant
package.name = voiceassistant
package.domain = org.voiceassistant

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 0.1
requirements = python3,kivy,openssl,requests

[buildozer]
log_level = 2

# Android 特定配置
[app:android]
api = 33
minapi = 21
ndk = 25b
android.accept_sdk_license = True