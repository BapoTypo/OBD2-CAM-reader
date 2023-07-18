@echo off

REM Change the current directory to the specified location
cd /d "C:\Program Files (x86)\Minimal ADB and Fastboot"

REM Execute the "adb devices" command
adb devices

REM Execute the "adb forward" command
adb forward tcp:5277 tcp:5277

REM Executes Android auto
cd "C:/Users/Taken/AppData/Local/Android/Sdk/extras/google/auto"
start desktop-head-unit.exe -c C:\Users\Taken\AppData\Local\Android\Sdk\extras\google\auto\config\default.ini 
