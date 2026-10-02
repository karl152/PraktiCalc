#!/bin/dash

# PraktiCalc © 2024-2026 Karl Wesseler
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0-only

set -eu

echo "checking for dependencies"
for dep in dh dpkg-buildpackage
do
    if command -v "$dep" >/dev/null 2>&1
    then
        echo "FOUND: $dep"
    else
        echo "ERROR: $dep appears to be missing!"
        false
    fi
done

chmod +x debian/rules
cp src/prakticalc_karl152/PLEL.png linux-pkg-builds/debian/prakticalc/usr/share/icons/hicolor/128x128/apps/de.karl_52.PraktiCalc.PLEL.png

if [ "$#" -lt 1 ]; then
    echo "Please specify a build mode (deb or dsc)."
    false
fi

if [ "$1" = "deb" ]; then
    dpkg-buildpackage --no-sign --build=binary
    rm -rv debian/.debhelper/ debian/prakticalc debian/debhelper-build-stamp debian/files debian/prakticalc.substvars
elif [ "$1" = "dsc" ]; then
    dpkg-buildpackage --build=source
    rm -v debian/files
else
    echo "Please specify a build mode (deb or dsc)."
fi

chmod -x debian/rules
rm linux-pkg-builds/debian/prakticalc/usr/share/icons/hicolor/128x128/apps/de.karl_52.PraktiCalc.PLEL.png
