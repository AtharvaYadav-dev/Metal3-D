@echo off
cd /d "%~dp0GalvoUI_with_calibration_page"
"C:\Program Files\Python312\python.exe" main.py
if errorlevel 1 pause
