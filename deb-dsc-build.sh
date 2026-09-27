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

if [ "$#" -lt 1 ]; then
    echo "Please specify a build mode (deb or dsc)."
    false
fi

if [ "$1" = "deb" ]; then
    dpkg-buildpackage --no-sign --build=binary
    chmod -x debian/rules
    rm -rv debian/.debhelper/ debian/prakticalc debian/debhelper-build-stamp debian/files debian/prakticalc.substvars
elif [ "$1" = "dsc" ]; then
    dpkg-buildpackage --build=source
    chmod -x debian/rules
    rm -v debian/files
else
    echo "Please specify a build mode (deb or dsc)."
fi
