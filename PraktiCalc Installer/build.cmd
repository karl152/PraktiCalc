@echo off

rem PraktiCalc - a calculator with GUI I started at my student internship in 2024
rem Copyright (C) 2024-2025 Karl "karl152"
rem
rem This program is free software: you can redistribute it and/or modify
rem it under the terms of the GNU General Public License as published by
rem the Free Software Foundation, version 3.
rem
rem This program is distributed in the hope that it will be useful,
rem but WITHOUT ANY WARRANTY; without even the implied warranty of
rem MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
rem See the GNU General Public License for more details.
rem
rem You should have received a copy of the GNU General Public License
rem along with this program. If not, see <https://www.gnu.org/licenses/>.

echo Compressing content into ZIP
rem Using 7z because Compress-Archive isn't present in PowerShell on Windows 7
"C:\Program Files\7-Zip\7z.exe" a .\PraktiCalcProgramContent.zip .\content\*
echo Building EXE
python -m PyInstaller prakticalc-installer.py --onefile --windowed --add-data PraktiCalcBanner.png:. --add-data PraktiCalcProgramContent.zip:. --add-data ..\LICENSE:. --uac-admin --icon ..\PraktiCalculator.ico
echo copying final build
robocopy .\dist .. prakticalc-installer.exe
echo Cleaning up directories and files
rmdir /S /Q dist
rmdir /S /Q build
del prakticalc-installer.spec
del PraktiCalcProgramContent.zip
del content\prakticalc.exe
del content\PraktiCalcUninstaller.exe