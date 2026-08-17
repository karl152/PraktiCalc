-- PraktiCalc © 2024-2026 Karl Wesseler
-- Licensed under the GNU General Public License v3.0.
-- See https://www.gnu.org/licenses/gpl-3.0.txt for details.
-- SPDX-License-Identifier: GPL-3.0-only

-- Build Requirements:
-- - modern Python with tkinter (not the macOS system Python 3.9)
-- - ttkthemes
-- - pyinstaller

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
