-- PraktiCalc © 2024-2026 Karl Wesseler
-- Licensed under the GNU General Public License v3.0.
-- See https://www.gnu.org/licenses/gpl-3.0.txt for details.
-- SPDX-License-Identifier: GPL-3.0-only

-- Build Requirements:
-- - modern Python with tkinter (not the macOS system Python 3.9)
-- - ttkthemes
-- - pyinstaller
-- - patch (from the Xcode Command Line Tools or from somewhere else)

-- check if patch is present
try
	do shell script "which patch"
on error
	display dialog "patch seems to be missing, try installing the Xcode Command Line Tools or another implementation" with icon stop
	error number -128
end try

-- check if Python version is NOT 3.9
set PyVersionString to do shell script "python --version"
if PyVersionString contains "3.9." then
	display dialog "You are using an outdated version of Python, which also may be the macOS system Python installation! Please read the build requirements in macos-build.applescript" with icon stop
	error number -128
end if

-- check if PyInstaller is present
try
	do shell script "python -m PyInstaller --version"
on error
	display dialog "PyInstaller seems to be missing. Please read the build requirements in macos-build.applescript" with icon stop
	error number -128
end try

-- check if TkInter and ttkthemes are present
try
	do shell script "python -c 'import tkinter, ttkthemes'"
on error
	display dialog "Missing Python modules: either tkinter or ttkthemes or both modules are currently missing!" with icon stop
	error number -128
end try

-- set workdir to current directory
set workdir to do shell script "pwd"

-- ask for version number
display dialog "Please enter the PraktiCalc version:" default answer "" with title "set PraktiCalcVersion"
set PraktiCalcVersion to text returned of result
set FileName to "prakticalc-" & PraktiCalcVersion & "-aarch64"

-- build PraktiCalc
do shell script "python3 -m PyInstaller --onefile --windowed --strip --clean prakticalc.py --add-data PraktiCalculator.png:. --add-data PraktiCalculator_icon.png:. --add-data PraktiCalculator_icon.xbm:. --add-data PraktiCalculator_icon_inverted.xbm:. --add-data python-powered.png:. --add-data PraktiCalc-MacOS.png:. --name " & FileName & " --icon PraktiCalc-MacOS.png"
tell application "Finder"
	-- move prakticalc.app to working directory
	set build to POSIX file (workdir & "/dist/" & FileName & ".app") as alias
	move build to POSIX file workdir as alias
	-- delete build files
	delete (POSIX file (workdir & "/build") as alias)
	delete (POSIX file (workdir & "/dist") as alias)
	delete (POSIX file (workdir & "/" & FileName & ".spec") as alias)
end tell

-- patch Info.plist
do shell script "cd " & FileName & ".app/Contents/" & " && patch Info.plist < ../../InfoPlist.patch && sed -i '' 's/0.0.0/" & PraktiCalcVersion & "/g' Info.plist"

-- move app into builds directory
tell application "Finder"
	if not (exists folder "build" of POSIX file workdir) then
		make new folder at POSIX file workdir with properties {name:"builds"}
	end if
	move (POSIX file (workdir & "/" & FileName & ".app") as alias) to POSIX file (workdir & "/builds") as alias
end tell
