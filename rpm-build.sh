#!/bin/sh

# PraktiCalc © 2024-2026 Karl "karl152"
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0

# REQUIREMENTS
# - Fedora
# - rpm-build
# - rpmdevtools
# - python3-devel
# - python3-tkinter

# clean up from previous build
rm -rf ~/rpmbuild/

# copy Debian directory
cd linux-pkg-builds/
cp -r debian/ rpm/
rm -rf rpm/prakticalc/DEBIAN/
rm -rf rpm/prakticalc/usr/share/doc/
sed -i "s/dash/sh/g"  rpm/prakticalc/usr/bin/prakticalc || exit 1

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
