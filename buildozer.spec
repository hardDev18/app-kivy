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

# تنظیمات حیاتی اندروید
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.accept_sdk_license = True
android.ndk_path = 
android.sdk_path = 

# معماری پردازنده (فقط یه معماری برای سرعت بیشتر)
android.arch = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
