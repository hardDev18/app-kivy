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

# تنظیمات اندروید - بدون هیچ warning
android.api = 31
android.minapi = 21
android.ndk = 25.2.9519653
android.accept_sdk_license = True

# تغییر مهم: android.arch -> android.archs
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
