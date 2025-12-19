# PraktiCalc © 2024-2025 Karl "karl152"
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.

$mode = $args[0]

if ($mode -eq "portable"){
Write-Host "Building portable executable for PraktiCalc..."
Remove-Item .\prakticalc.exe -ErrorAction SilentlyContinue
python.exe -m PyInstaller .\prakticalc.py --onefile --clean --windowed --add-data PraktiCalculator_icon.png:. --add-data PraktiCalculator_icon.xbm:. --add-data PraktiCalculator_icon_inverted.xbm:. --add-data info.vbs:. --add-data error.vbs:. --icon PraktiCalculator.ico
Copy-Item .\dist\prakticalc.exe .
Write-Host "Cleaning up..."
Remove-Item .\dist -Recurse -Force
Remove-Item .\build -Recurse -Force
Remove-Item .\prakticalc.spec
Write-Host "Done!"
}
elseif ($mode -eq "installer"){
Write-Host "Building installer for PraktiCalc..."
Write-Host "[1/3] Building PraktiCalc..."
Remove-Item .\prakticalc-installer.exe -ErrorAction SilentlyContinue
python.exe -m PyInstaller .\prakticalc.py --onedir --clean --windowed --add-data PraktiCalculator_icon.png:. --add-data PraktiCalculator_icon.xbm:. --add-data PraktiCalculator_icon_inverted.xbm:. --add-data info.vbs:. --add-data error.vbs:. --icon PraktiCalculator.ico
Copy-Item .\dist\prakticalc\* '.\PraktiCalc Installer\content' -Recurse -Verbose
Remove-Item .\dist -Recurse -Force
Remove-Item .\build -Recurse -Force
Remove-Item .\prakticalc.spec
Write-Host "[2/3] Building Uninstaller..."
Set-Location '.\PraktiCalc Uninstaller'
python.exe -m PyInstaller .\PraktiCalcUninstaller.py --onedir --clean --windowed --icon ..\PraktiCalculatorMono.ico
Copy-Item .\dist\PraktiCalcUninstaller '..\PraktiCalc Installer\content' -Recurse -Verbose
Remove-Item .\dist -Recurse -Force
Remove-Item .\build -Recurse -Force
Remove-Item .\PraktiCalcUninstaller.spec
Set-Location '..\PraktiCalc Installer'
Write-Host "[3/3] Building Installer..."
try {Compress-Archive -Path .\content\* -DestinationPath .\PraktiCalcProgramContent.zip -CompressionLevel Optimal -Verbose}
catch {& "C:\Program Files\7-Zip\7z.exe" a .\PraktiCalcProgramContent.zip .\content\* -mx9}
python.exe -m PyInstaller .\prakticalc-installer.py --onefile --clean --windowed --add-data PraktiCalcBanner.png:. --add-data PraktiCalcProgramContent.zip:. --add-data .\narrator.vbs:. --add-data ..\LICENSE:. --uac-admin --icon ..\PraktiCalculator.ico
Copy-Item .\dist\prakticalc-installer.exe ..
Remove-Item .\dist -Recurse -Force
Remove-Item .\build -Recurse -Force
Remove-Item .\prakticalc-installer.spec
Remove-Item .\PraktiCalcProgramContent.zip
Remove-Item .\content\prakticalc.exe
Remove-Item .\content\PraktiCalcUninstaller -Recurse -Force
Remove-Item .\content\_internal -Recurse -Force
Write-Host "Done!"
}
else{Write-Host "No valid build mode selected. Available modes: portable, installer"}