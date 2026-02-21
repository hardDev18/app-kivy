[app]
title = ماشین حساب
package.name = mashinhesab
package.domain = ir.hosseinhamidy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# تنظیمات اندروید - بدون android.sdk
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
