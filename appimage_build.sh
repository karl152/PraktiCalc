#!/bin/sh

# PraktiCalc © 2024-2026 Karl Wesseler
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0-only

# REQUIREMENTS FOR DEBIAN
# - wget2/wget/curl
# - python3
# - python3-tk
# - python3-ttkthemes
# - python3-pyinstaller

set -eu

# check for Python 3 and PyInstaller
if command -v python3
then
    echo "found Python 3"
else
    echo "ERROR: Python 3 seems to be missing"
    false
fi
if python3 -m PyInstaller --version >/dev/null 2>&1
then
    echo "found PyInstaller"
else
    echo "ERROR: PyInstaller is missing"
    false
fi

# check for download tools
dltcount=3
for dlt in curl wget wget2
do
    if command -v "$dlt"; then
        echo "FOUND: $dlt"
    else
        echo "didn't find $dlt"
        dltcount="$((dltcount-1))"
    fi
done
if [ $dltcount -le 0 ]; then
    echo "ERROR: wget2, wget and curl weren't found, but one of them is required for this script to work"
    false
fi

# check for tkinter, ttkthemes
echo "checking for Python modules"
for PythonModule in tkinter ttkthemes
do
    if python3 -c "import $PythonModule" >/dev/null 2>&1
    then
        echo "FOUND: $PythonModule"
    else
        echo "ERROR: $PythonModule appears to be missing!"
        false
    fi
done

echo "Cleaning"
rm build/PraktiCalc-$(uname -m).AppImage || echo "no previous AppImage to remove"
rm build/PraktiCalc-$(uname -m).AppImage.zsync || true

mkdir -p linux-pkg-builds/AppImage/de.karl_52.PraktiCalc.AppDir/usr/bin

echo "Building Executable"
python3 -m PyInstaller prakticalc.py --onedir --strip --clean --add-data PraktiCalculator_icon.png:. --add-data PraktiCalculator_icon.xbm:. --add-data PraktiCalculator_icon_inverted.xbm:. --add-data python-powered.png:. --add-data /usr/share/tcltk/ttkthemes:ttkthemes --icon PraktiCalculator.ico
cd ./dist/prakticalc/_internal/
echo "Cleaning libraries..."
rm -v libX11.so.6 libXext.so.6 libXft.so.2 libXrender.so.1 libXau.so.6 libXdmcp.so.6 libfontconfig.so.1 libfreetype.so.6 libbz2.so.1.0 libbrotlicommon.so.1 libbrotlidec.so.1 libbrotlienc.so.1 libzstd.so.1 libz.so.1 libyaml-0.so.2 libtiff.so.6 libjpeg.so.62 libpng16.so.16 libsharpyuv.so.0 libwebp.so.7 libwebpmux.so.3 libwebpdemux.so.2 libimagequant.so.0 liblcms2.so.2 libopenjp2.so.7 || true
cd ../../../
mv ./dist/prakticalc/* ./linux-pkg-builds/AppImage/de.karl_52.PraktiCalc.AppDir/usr/bin/
chmod +x ./linux-pkg-builds/AppImage/de.karl_52.PraktiCalc.AppDir/AppRun
chmod +x ./linux-pkg-builds/AppImage/de.karl_52.PraktiCalc.AppDir/usr/bin/prakticalc
echo ""
echo "------------------------------------------------------------------------------------"
echo "The script will now download appimagetool from https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-$(uname -m).AppImage. If you don't want that, press CTRL+C now."
echo "------------------------------------------------------------------------------------"
sleep 10
echo "Downloading appimagetool"
wget2 -c https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-$(uname -m).AppImage || wget -c https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-$(uname -m).AppImage || curl -# -L https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-$(uname -m).AppImage -o appimagetool-$(uname -m).AppImage
chmod +x appimagetool-$(uname -m).AppImage
mv ./appimagetool-$(uname -m).AppImage ./linux-pkg-builds/AppImage/

echo "Building AppImage"
cd ./linux-pkg-builds/AppImage
./appimagetool-$(uname -m).AppImage -u "zsync|https://karl-52.de/PraktiCalc/latest/PraktiCalc-$(uname -m).AppImage.zsync" de.karl_52.PraktiCalc.AppDir

echo "Cleaning"
rm appimagetool-$(uname -m).AppImage
cd ../..
rm -rf ./linux-pkg-builds/AppImage/de.karl_52.PraktiCalc.AppDir/usr/bin
rm -rf dist/
rm -rf build/
rm prakticalc.spec

echo "Moving to build folder"
mkdir build
mv linux-pkg-builds/AppImage/PraktiCalc-$(uname -m).AppImage build/
mv linux-pkg-builds/AppImage/PraktiCalc-$(uname -m).AppImage.zsync build/

echo "Done!"
