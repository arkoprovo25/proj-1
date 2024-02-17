[app]

# (str) Title of your application
title = MovieManager

# (str) Package name
package.name = moviemanager

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*,fonts/*

# (str) Application versioning (method 1)
version = 0.1

# (list) List of service to declare
services = NAME:NAME:NAME

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Presplash of the application
presplash.filename = %(source.dir)s/images/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/images/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (list) Python requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = kivy

# (str) iOS framework to include (a comma separated list)
# ios.frameworks = 

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*,fonts/*

# (str) Application main file in python
#main.py

# (list) List of import name to exclude from the compilation
#p4a.exclude =

# (str) The directory in which python-for-android should build its artifacts
#p4a.build_dir = 

# (str) Path to a custom distribution
#p4a.dist_name = 

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
#android.apptheme = 

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (str) iOS project directory
#ios.project_dir = %(source.dir)s

# (str) iOS main.py file
#ios.main_py = %(source.dir)s/main.py

# (str) iOS icon filename (without extension)
#ios.icon.filename = %(source.dir)s/icon

# (str) iOS app bundle identifier
#ios.bundle_identifier = org.example.myapp

# (str) Window border size
#border = 10

# (bool) Do not warn about multiple classes found during build (filenamemismatches)
#nowarnfilenamemismatch = False

# (list) Application requirements
# requirements = sqlite3,kivy

# (str) Presplash background color (for new android toolchain)
# (black/white/gray/lightgray)
#presplash.color = #FFFFFF

# (str) Presplash background image (for new android toolchain)
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon background color (for new android toolchain)
#icon.background_color = #FFFFFF

# (str) Icon foreground image source (for new android toolchain)
#icon.foreground_color = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
#orientation = portrait
