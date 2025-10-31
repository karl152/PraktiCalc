#!/bin/bash

# PraktiCalc © 2024-2025 Karl "karl152"
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.

# clean up last build
rm linux-pkg-builds/debian/prakticalc.deb

# copy files
cp ./prakticalc.py linux-pkg-builds/debian/prakticalc/usr/share/prakticalc/
cp ./LICENSE linux-pkg-builds/debian/prakticalc/usr/share/prakticalc/
cp ./PraktiCalculator_icon_inverted.xbm linux-pkg-builds/debian/prakticalc/usr/share/prakticalc/
cp ./PraktiCalculator_icon.png linux-pkg-builds/debian/prakticalc/usr/share/prakticalc/
cp ./PraktiCalculator_icon.xbm linux-pkg-builds/debian/prakticalc/usr/share/prakticalc/

# edit changelog
gunzip linux-pkg-builds/debian/prakticalc/usr/share/doc/prakticalc/changelog.gz
nano linux-pkg-builds/debian/prakticalc/usr/share/doc/prakticalc/changelog
gzip -n -9 linux-pkg-builds/debian/prakticalc/usr/share/doc/prakticalc/changelog

# set permissions
cd linux-pkg-builds/debian/prakticalc/
find usr -type d -exec chmod 755 {} \;
find usr -type f -exec chmod 644 {} \;
chmod 755 usr/bin/prakticalc

# build package
cd ..
dpkg-deb --build --root-owner-group prakticalc/

# clean up
rm ./prakticalc/usr/share/prakticalc/*

# show errors if lintian is installed
lintian prakticalc.deb
