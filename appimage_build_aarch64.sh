#!/bin/bash

# PraktiCalc © 2024-2025 Karl "karl152"
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.

echo "Cleaning"
rm linux-pkg-builds/AppImage/PraktiCalc-x86_64.AppImage

mkdir -p linux-pkg-builds/AppImage/PraktiCalc.AppDir/usr/bin

echo "Building Executable"
python3 -m PyInstaller prakticalc.py --onedir --strip --clean --add-data PraktiCalculator_icon.png:. --add-data PraktiCalculator_icon.xbm:. --add-data PraktiCalculator_icon_inverted.xbm:. --add-data /usr/share/tcltk/ttkthemes:ttkthemes --icon PraktiCalculator.ico
cd ./dist/prakticalc/_internal/
echo "Cleaning libraries..."
rm libX11.so.6
rm libXext.so.6
rm libXft.so.2
rm libXrender.so.1
rm libXau.so.6
rm libXdmcp.so.6
rm libfontconfig.so.1
rm libfreetype.so.6
rm libbz2.so.1.0
rm libbrotlicommon.so.1
rm libbrotlidec.so.1
rm libbrotlienc.so.1
rm libzstd.so.1
rm libz.so.1
rm libyaml-0.so.2
rm libtiff.so.6
rm libjpeg.so.62
rm libpng16.so.16
rm libsharpyuv.so.0
rm libwebp.so.7
rm libwebpmux.so.3
rm libwebpdemux.so.2
rm libimagequant.so.0
rm liblcms2.so.2
rm libopenjp2.so.7
cd ../../../
mv ./dist/prakticalc/* ./linux-pkg-builds/AppImage/PraktiCalc.AppDir/usr/bin/
chmod +x ./linux-pkg-builds/AppImage/PraktiCalc.AppDir/AppRun
chmod +x ./linux-pkg-builds/AppImage/PraktiCalc.AppDir/usr/bin/prakticalc
echo ""
echo "------------------------------------------"
echo "The script will now download appimagetool from https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-aarch64.AppImage. If you don't want that, press CTRL+C now."
echo "------------------------------------------"
sleep 10
echo "Downloading appimagetool"
wget https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-aarch64.AppImage
chmod +x appimagetool-aarch64.AppImage
mv ./appimagetool-aarch64.AppImage ./linux-pkg-builds/AppImage/

echo "Building AppImage"
cd ./linux-pkg-builds/AppImage
./appimagetool-aarch64.AppImage PraktiCalc.AppDir

echo "Cleaning"
rm appimagetool-aarch64.AppImage
cd ../..
rm -rf ./linux-pkg-builds/AppImage/PraktiCalc.AppDir/usr
rm -rf dist/
rm -rf build/
rm prakticalc.spec
