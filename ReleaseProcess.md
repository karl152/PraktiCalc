## PraktiCalc Release Process
This is a checklist for me to make sure I don't forget anything.
* check if copyright years are correct
* make sure that version numbers are current (files with version numbers: `prakticalc.py`, `PraktiCalc Installer/prakticalc-installer.py`, `linux-pkg-builds/debian/prakticalc/DEBIAN/control`, `SECURITY.md`, `linux-pkg-builds/rpmdata/prakticalc.spec`, `InfoPlist.patch`)
* update version banner in the Windows Installer
* update README and AppStream metadata (both) to show current screenshot
* make sure the README is fine
* write changelog
* update Fedora RPM changelog
* build Debian package with the new changelog
* update Debian manpage
* build packages and test them
* make new GitHub release and upload builds
* make sure the repository’s social media preview is up-to-date
* update the [SourceForge](https://sourceforge.net/p/prakticalc/code/ci/main/tree/) and [Launchpad](https://git.launchpad.net/~karl52/+git/PraktiCalc) git mirrors
* make sure [the SourceForge page](https://sourceforge.net/projects/prakticalc/) is fine in general
* update the webserver used for AppImageUpdate
* update Ubuntu PPAs [karl52/prakticalc](https://launchpad.net/~karl52/+archive/ubuntu/prakticalc), [karl52/prakticalc-lts](https://launchpad.net/~karl52/+archive/ubuntu/prakticalc-lts)
