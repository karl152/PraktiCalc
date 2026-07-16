#!/bin/sh

# PraktiCalc © 2024-2026 Karl Wesseler
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0-only

# required TinyCore extensions to build: squashfs-tools.tcz
# required TinyCore extensions to run: python3.14, tk8.6

read -p "PraktiCalc Version: " PraktiCalcVersion
echo "Cleaning up from last build..."
rm prakticalc-$PraktiCalcVersion.tcz*
echo "Creating directories..."
mkdir -p linux-pkg-builds/tce/usr/share/prakticalc
mkdir -p linux-pkg-builds/tce/usr/bin
echo "Copying files..."
cp linux-pkg-builds/debian/prakticalc/usr/bin/prakticalc linux-pkg-builds/tce/usr/bin/
sed -i "s/dash/sh/g" linux-pkg-builds/tce/usr/bin/prakticalc
sed -i "s|/usr/bin/python3|/usr/local/bin/python3.14|g" linux-pkg-builds/tce/usr/bin/prakticalc
cp prakticalc.py linux-pkg-builds/tce/usr/share/prakticalc/
cp *_icon* linux-pkg-builds/tce/usr/share/prakticalc/
cp python-powered.png linux-pkg-builds/tce/usr/share/prakticalc/
cp -r linux-pkg-builds/debian/prakticalc/usr/share/applications/ linux-pkg-builds/tce/usr/share/applications
cp -r linux-pkg-builds/debian/prakticalc/usr/share/icons/ linux-pkg-builds/tce/usr/share/icons
cp LICENSE linux-pkg-builds/tce/usr/share/prakticalc/
chmod +x linux-pkg-builds/tce/usr/bin/prakticalc
echo "creating prakticalc.tcz..."
cd linux-pkg-builds
mksquashfs tce/ prakticalc-$PraktiCalcVersion.tcz
echo "deleting build folder..."
rm -rf tce/
mv prakticalc-$PraktiCalcVersion.tcz ../
cd ..
echo "python3.14.tcz" > prakticalc-$PraktiCalcVersion.tcz.dep
echo "tk8.6.tcz" >> prakticalc-$PraktiCalcVersion.tcz.dep
echo "created dependency file"
echo "Title: 		PraktiCalc" > prakticalc-$PraktiCalcVersion.tcz.info
echo "Description:	A Practical Calculator written in Python" >> prakticalc-$PraktiCalcVersion.tcz.info
echo "Version:	$PraktiCalcVersion" >> prakticalc-$PraktiCalcVersion.tcz.info
echo 'Author:		Karl Wesseler' >> prakticalc-$PraktiCalcVersion.tcz.info
echo "License:	GPL-3.0" >> prakticalc-$PraktiCalcVersion.tcz.info
echo "Dependencies:	python3.14.tcz tk8.6.tcz" >> prakticalc-$PraktiCalcVersion.tcz.info
echo "created info file"
md5sum prakticalc-$PraktiCalcVersion.tcz > prakticalc-$PraktiCalcVersion.tcz.md5.txt
echo "created md5 checksum file"
echo "Build complete!"
