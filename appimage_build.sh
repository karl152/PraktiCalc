#!/bin/bash

echo "Cleaning"
rm linux-pkg-builds/AppImage/PraktiCalc-x86_64.AppImage

echo "Building Executable"
python3 -m PyInstaller prakticalc.py --onedir --strip --clean --add-data PraktiCalculator_icon.png:. --add-data PraktiCalculator_icon.xbm:. --add-data PraktiCalculator_icon_inverted.xbm:. --add-data /usr/share/tcltk/ttkthemes:ttkthemes --icon PraktiCalculator.ico
mv ./dist/prakticalc/* ./linux-pkg-builds/AppImage/PraktiCalc.AppDir/usr/bin/
chmod +x ./linux-pkg-builds/AppImage/PraktiCalc.AppDir/usr/bin/prakticalc
echo ""
echo "------------------------------------------"
echo "The script will now download appimagetool from https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-x86_64.AppImage. If you don't want that, press CTRL+C now."
echo "------------------------------------------"
sleep 10
echo "Downloading appimagetool"
wget https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-x86_64.AppImage
chmod +x appimagetool-x86_64.AppImage
mv ./appimagetool-x86_64.AppImage ./linux-pkg-builds/AppImage/

echo "Building AppImage"
cd ./linux-pkg-builds/AppImage
./appimagetool-x86_64.AppImage PraktiCalc.AppDir

echo "Cleaning"
rm appimagetool-x86_64.AppImage
cd ../..
rm -rf ./linux-pkg-builds/AppImage/PraktiCalc.AppDir/usr/bin/*
rm -rf dist/
rm -rf build/
rm prakticalc.spec
