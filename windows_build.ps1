# PraktiCalc © 2024-2026 Karl Wesseler
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0-only

# REQUIREMENTS
# - Windows 7 or newer
# - PowerShell 2+ with 7-Zip or PowerShell 5/7
# - Python 3.8 or newer with tkinter and pip
# - PIP Modules: ttkthemes, pyinstaller

$mode = $args[0]
$winVersion = [System.Environment]::OSVersion.Version
if ($winVersion.major -eq 6 -and $winVersion.minor -eq 1) {
    $winVersionString = "win7"
} elseif ($winVersion.major -eq 10) {
    $winVersionString = "win"
} else {
    $winVersionString = "winX"
}

if ($mode -eq "portable"){
$PraktiCalcVersion = Read-Host "PraktiCalc Version"
Write-Host "Building portable executable for PraktiCalc..."
Remove-Item .\builds\prakticalc-$PraktiCalcVersion-$winVersionString-amd64-portable.zip -ErrorAction SilentlyContinue
python.exe -m PyInstaller .\prakticalc.py --onedir --clean --windowed --add-data PraktiCalculator_icon.png:. --add-data PraktiCalculator_icon.xbm:. --add-data PraktiCalculator_icon_inverted.xbm:. --add-data python-powered.png:. --add-data info.vbs:. --add-data error.vbs:. --icon PraktiCalculator.ico
New-Item -ItemType Directory .\builds -ErrorAction SilentlyContinue
try {Compress-Archive -Path .\dist\prakticalc\* -DestinationPath .\builds\prakticalc-$PraktiCalcVersion-$winVersionString-amd64-portable.zip -CompressionLevel Optimal -Verbose}
catch {& "C:\Program Files\7-Zip\7z.exe" a .\builds\prakticalc-$PraktiCalcVersion-$winVersionString-amd64-portable.zip .\dist\prakticalc\* -mx9}
Write-Host "Cleaning up..."
Remove-Item .\dist -Recurse -Force
Remove-Item .\build -Recurse -Force
Remove-Item .\prakticalc.spec
Write-Host "Done!"
}
elseif ($mode -eq "installer"){
$PraktiCalcVersion = Read-Host "PraktiCalc Version"
Write-Host "Building installer for PraktiCalc..."
Write-Host "[1/3] Building PraktiCalc..."
Remove-Item .\builds\prakticalc-$PraktiCalcVersion-$winVersionString-amd64-installer.exe -ErrorAction SilentlyContinue
Copy-Item .\LICENSE '.\PraktiCalc Installer\content' -Verbose
python.exe -m PyInstaller .\prakticalc.py --onedir --clean --windowed --add-data PraktiCalculator_icon.png:. --add-data PraktiCalculator_icon.xbm:. --add-data PraktiCalculator_icon_inverted.xbm:. --add-data python-powered.png:. --add-data info.vbs:. --add-data error.vbs:. --icon PraktiCalculator.ico
Copy-Item .\dist\prakticalc\* '.\PraktiCalc Installer\content' -Recurse -Verbose
Remove-Item .\dist -Recurse -Force
Remove-Item .\build -Recurse -Force
Remove-Item .\prakticalc.spec
Write-Host "[2/3] Building Uninstaller..."
Set-Location '.\PraktiCalc Uninstaller'
python.exe -m PyInstaller .\PraktiCalcUninstaller.py --onedir --clean --windowed --uac-admin --icon ..\PraktiCalculatorMono.ico
Copy-Item .\dist\PraktiCalcUninstaller\* '..\PraktiCalc Installer\content' -Recurse -Verbose
Remove-Item .\dist -Recurse -Force
Remove-Item .\build -Recurse -Force
Remove-Item .\PraktiCalcUninstaller.spec
Set-Location '..\PraktiCalc Installer'
Write-Host "[3/3] Building Installer..."
try {Compress-Archive -Path .\content\* -DestinationPath .\PraktiCalcProgramContent.zip -CompressionLevel Optimal -Verbose}
catch {& "C:\Program Files\7-Zip\7z.exe" a .\PraktiCalcProgramContent.zip .\content\* -mx9}
python.exe -m PyInstaller .\prakticalc-installer.py --onefile --clean --windowed --add-data PraktiCalcBanner.png:. --add-data PraktiCalcProgramContent.zip:. --add-data .\narrator.vbs:. --add-data ..\LICENSE:. --uac-admin --icon ..\PraktiCalculator.ico
New-Item -ItemType Directory ..\builds -ErrorAction SilentlyContinue
Move-Item .\dist\prakticalc-installer.exe ..\builds\prakticalc-$PraktiCalcVersion-$winVersionString-amd64-installer.exe
Remove-Item .\dist -Recurse -Force
Remove-Item .\build -Recurse -Force
Remove-Item .\prakticalc-installer.spec
Remove-Item .\PraktiCalcProgramContent.zip
Remove-Item .\content\prakticalc.exe
Remove-Item .\content\PraktiCalcUninstaller.exe
Remove-Item .\content\_internal -Recurse -Force
Remove-Item .\content\LICENSE
Write-Host "Done!"
}
else{Write-Host "No valid build mode selected. Available modes: portable, installer"}
