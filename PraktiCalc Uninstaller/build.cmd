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

python -m PyInstaller PraktiCalcUninstaller.py --onefile --windowed --icon ..\PraktiCalculatorMono.ico
robocopy .\dist "..\PraktiCalc Installer\content" PraktiCalcUninstaller.exe
rmdir /S /Q dist
rmdir /S /Q build
del PraktiCalcUninstaller.spec