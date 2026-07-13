#!/bin/dash

# PraktiCalc © 2024-2026 Karl Wesseler
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0-only

PraktiCalcDir=$(pwd)

setupDebDir() {
    mkdir -p debian/source
    cp linux-pkg-builds/debian/prakticalc/usr/share/doc/prakticalc/copyright debian/
    gunzip -v linux-pkg-builds/debian/prakticalc/usr/share/man/man1/prakticalc.1.gz
    gunzip -vc linux-pkg-builds/debian/prakticalc/usr/share/doc/prakticalc/changelog.gz > debian/changelog
    echo "3.0 (native)" > debian/source/format
    echo "linux-pkg-builds/debian/prakticalc/usr/share/man/man1/prakticalc.1" > debian/prakticalc.manpages
    
cat > debian/control <<EOF
Source: prakticalc
Maintainer: Karl <karldpbkz@gmail.com>
Section: utils
Priority: optional
Build-Depends: debhelper-compat (=13)
Standards-Version: 4.7.2.0
Homepage: https://github.com/karl152/PraktiCalc

Package: prakticalc
Section: utils
Priority: optional
Architecture: all
Description: practical calculator written in Python
 A practical calculator written in Python with Tkinter and TTK
Depends: python3 (>= 3.8), python3-tk
Recommends: python3-ttkthemes
Suggests: x11-utils, gxmessage, yad, kdialog, zenity
Provides: prakticalc
Replaces: prakticalc
Conflicts: prakticalc
Homepage: https://github.com/karl152/PraktiCalc
EOF

cat > debian/install <<EOF
prakticalc.py usr/share/prakticalc
LICENSE usr/share/prakticalc
PraktiCalculator_icon_inverted.xbm usr/share/prakticalc
PraktiCalculator_icon.png usr/share/prakticalc
PraktiCalculator_icon.xbm usr/share/prakticalc
python-powered.png usr/share/prakticalc
linux-pkg-builds/debian/prakticalc/usr/bin/prakticalc usr/bin
linux-pkg-builds/debian/prakticalc/usr/share/applications/de.karl_52.PraktiCalc.desktop usr/share/applications
linux-pkg-builds/debian/prakticalc/usr/share/icons/hicolor/16x16/apps/de.karl_52.PraktiCalc.png usr/share/icons/hicolor/16x16/apps
linux-pkg-builds/debian/prakticalc/usr/share/icons/hicolor/32x32/apps/de.karl_52.PraktiCalc.png usr/share/icons/hicolor/32x32/apps
linux-pkg-builds/debian/prakticalc/usr/share/icons/hicolor/64x64/apps/de.karl_52.PraktiCalc.png usr/share/icons/hicolor/64x64/apps
linux-pkg-builds/debian/prakticalc/usr/share/icons/hicolor/128x128/apps/de.karl_52.PraktiCalc.png usr/share/icons/hicolor/128x128/apps
linux-pkg-builds/debian/prakticalc/usr/share/icons/hicolor/256x256/apps/de.karl_52.PraktiCalc.png usr/share/icons/hicolor/256x256/apps
linux-pkg-builds/debian/prakticalc/usr/share/icons/hicolor/512x512/apps/de.karl_52.PraktiCalc.png usr/share/icons/hicolor/512x512/apps
linux-pkg-builds/debian/prakticalc/usr/share/metainfo/de.karl_52.PraktiCalc.metainfo.xml usr/share/metainfo
EOF

cat > debian/rules <<"EOF"
#!/usr/bin/make -f

%:
	dh $@
EOF
chmod +x debian/rules
}

if [ "$1" = "deb" ]; then
    setupDebDir
    dpkg-buildpackage --build=binary
    gzip -n9v linux-pkg-builds/debian/prakticalc/usr/share/man/man1/prakticalc.1
    rm -rf debian/
elif [ "$1" = "dsc" ]; then
    setupDebDir
    dpkg-buildpackage --build=source
    gzip -n9v linux-pkg-builds/debian/prakticalc/usr/share/man/man1/prakticalc.1
    rm -rf debian/
else
    echo "Please specify a build mode (deb or dsc)."
fi
