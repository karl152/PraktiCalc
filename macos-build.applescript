-- PraktiCalc © 2024-2026 Karl Wesseler
-- Licensed under the GNU General Public License v3.0.
-- See https://www.gnu.org/licenses/gpl-3.0.txt for details.
-- SPDX-License-Identifier: GPL-3.0-only

-- Build Requirements:
-- - modern Python with tkinter (not the macOS system Python 3.9)
-- - ttkthemes
-- - pyinstaller

set workdir to do shell script "pwd"
set POSIXworkdir to POSIX file workdir

-- ask for version number
display dialog "Please enter the PraktiCalc version:" default answer "" with title "set PraktiCalcVersion"
set PraktiCalcVersion to text returned of result
set FileName to "prakticalc-" & PraktiCalcVersion & "-aarch64"

-- build PraktiCalc
do shell script "python3 -m PyInstaller --onefile --windowed --strip --clean prakticalc.py --add-data PraktiCalculator.png:. --add-data PraktiCalculator_icon.png:. --add-data PraktiCalculator_icon.xbm:. --add-data PraktiCalculator_icon_inverted.xbm:. --add-data python-powered.png:. --add-data PraktiCalc-MacOS.png:. --name " & FileName & " --icon PraktiCalc-MacOS.png"
tell application "Finder"
	-- move prakticalc.app to working directory
	set relativebuildpath to "/dist/" & FileName & ".app"
	set buildpath to workdir & relativebuildpath
	set build to POSIX file buildpath as alias
	move build to POSIXworkdir
	-- delete build files
	set relativebuildfolderpath to "/build"
	set relativedistfolderpath to "/dist"
	set relativespecfilepath to "/" & FileName & ".spec"
	set buildfolderpath to workdir & relativebuildfolderpath
	set distfolderpath to workdir & relativedistfolderpath
	set specfilepath to workdir & relativespecfilepath
	set buildfolder to POSIX file buildfolderpath as alias
	set distfolder to POSIX file distfolderpath as alias
	set specfile to POSIX file specfilepath as alias
	delete buildfolder
	delete distfolder
	delete specfile
end tell
