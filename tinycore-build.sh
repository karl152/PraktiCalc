#!/bin/sh
echo "Cleaning up from last build..."
rm prakticalc.tcz*
echo "Creating directories..."
mkdir -p linux-pkg-builds/tce/usr/share/prakticalc
mkdir -p linux-pkg-builds/tce/usr/bin
echo "Copying files..."
cp linux-pkg-builds/debian/prakticalc/usr/bin/prakticalc linux-pkg-builds/tce/usr/bin/
sed -i "s/bash/sh/g" linux-pkg-builds/tce/usr/bin/prakticalc
sed -i "s|/usr/bin/python3|/usr/local/bin/python3.9|g" linux-pkg-builds/tce/usr/bin/prakticalc
cp prakticalc.py linux-pkg-builds/tce/usr/share/prakticalc/
cp *_icon* linux-pkg-builds/tce/usr/share/prakticalc/
chmod +x linux-pkg-builds/tce/usr/bin/prakticalc
echo "creating prakticalc.tcz..."
cd linux-pkg-builds
mksquashfs tce/ prakticalc.tcz
echo "deleting build folder..."
rm -rf tce/
mv prakticalc.tcz ../
cd ..
echo "python3.9.tcz" > prakticalc.tcz.dep
echo "tk8.6.tcz" >> prakticalc.tcz.dep
echo "created dependency file"
echo "Title: 		PraktiCalc" > prakticalc.tcz.info
echo "Description:	A Practical Calculator written in Python" >> prakticalc.tcz.info
echo "Version:	1.3" >> prakticalc.tcz.info
echo 'Author:		Karl "karl152"' >> prakticalc.tcz.info
echo "License:	GPL-3.0" >> prakticalc.tcz.info
echo "created info file"
md5sum prakticalc.tcz > prakticalc.tcz.md5.txt
echo "created md5 checksum file"
echo "Build complete! Make sure to correct the version number in prakticalc.tcz.info"
