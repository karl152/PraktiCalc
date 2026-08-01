#!/bin/sh

# PraktiCalc © 2024-2026 Karl Wesseler
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0-only

# REQUIREMENTS
# - Fedora
# - rpm-build
# - rpmdevtools
# - python3-devel
# - python3-tkinter

set -eu

# check for dependencies
for cmd in python3 rpmdev-setuptree rpmbuild
do
    if command -v "$cmd"; then
        echo "FOUND: $cmd"
    else
        echo "didn't find $cmd"
        false
    fi
done

# check for tkinter
if python3 -c "import tkinter" >/dev/null 2>&1
then
    echo "FOUND: tkinter"
else
    echo "ERROR: tkinter appears to be missing!"
    false
fi

# clean up from previous build
rm -rf ~/rpmbuild/ || echo "no previous build to clean up"

# copy Debian directory
cd linux-pkg-builds/
cp -r debian/ rpm/
rm -rf rpm/prakticalc/DEBIAN/
rm -rf rpm/prakticalc/usr/share/doc/
sed -i "s/dash/sh/g"  rpm/prakticalc/usr/bin/prakticalc

# copy files
cd ..
mkdir  linux-pkg-builds/rpm/prakticalc/usr/share/prakticalc
cp ./prakticalc.py linux-pkg-builds/rpm/prakticalc/usr/share/prakticalc/
cp ./LICENSE linux-pkg-builds/rpm/prakticalc/usr/share/prakticalc/
cp ./PraktiCalculator_icon_inverted.xbm linux-pkg-builds/rpm/prakticalc/usr/share/prakticalc/
cp ./PraktiCalculator_icon.png linux-pkg-builds/rpm/prakticalc/usr/share/prakticalc/
cp ./PraktiCalculator_icon.xbm linux-pkg-builds/rpm/prakticalc/usr/share/prakticalc/
cp ./python-powered.png linux-pkg-builds/rpm/prakticalc/usr/share/prakticalc/

# set permissions
cd linux-pkg-builds/rpm/prakticalc/
find usr -type d -exec chmod 755 {} \;
find usr -type f -exec chmod 644 {} \;
chmod 755 usr/bin/prakticalc

# build package
cd ..
rpmdev-setuptree
tar czvf ~/rpmbuild/SOURCES/prakticalc.tar.gz ./
cd ..
cp rpmdata/prakticalc.spec ~/rpmbuild/SPECS/prakticalc.spec
cd ..
rpmbuild -ba ~/rpmbuild/SPECS/prakticalc.spec

# clean up
rm -rf linux-pkg-builds/rpm/
