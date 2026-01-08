## PraktiCalc Release Process
This is a checklist for me to make sure I don't forget anything.
* check if copyright years are correct
* make sure that version numbers are current (files with version numbers: ```prakticalc.py```, ```PraktiCalc Installer/prakticalc-installer.py```, ```linux-pkg-builds/debian/prakticalc/DEBIAN/control```)
* update version banner in the Windows Installer
* update README and AppStream metadata (both) to show current screenshot
* make sure the README is fine
* write changelog
* build Debian package with the new changelog
* update Debian manpage
* build packages and test them
* make new GitHub release and upload builds
