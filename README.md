# PraktiCalc
A practical calculator with GUI featuring a calculating history, an extension system & UI theming, as well as integration for many dialog tools.
<img alt="PraktiCalc Screenshot" src="https://raw.githubusercontent.com/karl152/PraktiCalcScreenshots/refs/heads/main/PraktiCalc1.5.png"/>

### Features
* calculation
* keyboard input
* trigonometry with different angle units
* hyperbolic functions
* calculating history
* customizable user interface
* support for many dialog tools
* extension system with preinstalled extensions
  * extension manager
  * plotter with zoom
  * decimal number converter
* support for Windows 7
* many more

### Get PraktiCalc
You can download PraktiCalc on the right at the Releases section. There should be a few files for each release there:
| file name example                       | description                                                      |
|-----------------------------------------|------------------------------------------------------------------|
| prakticalc-x.x-win-amd64-installer.exe  | PraktiCalc Installer for Windows 11 on 64-Bit x86 Processors     |
| prakticalc-x.x-win7-amd64-installer.exe | PraktiCalc Installer for Windows 7+ on 64-Bit x86 Processors     |
| prakticalc-x.x-win-amd64-portable.exe   | PraktiCalc for Windows 11 on 64-Bit x86 Processors (Portable)    |
| prakticalc-x.x-win7-amd64-portable.exe  | PraktiCalc for Windows 7+ on 64-Bit x86 Processors (Portable)    |
| prakticalc-x.x.deb                      | installable PraktiCalc Debian Package                            |
| prakticalc-x.x-amd64.AppImage           | portable AppImage file for Linux on 64-Bit x86 Processors        |
| prakticalc-x.x-aarch64.AppImage         | portable AppImage file for Linux on 64-Bit ARM Processors        |
| prakticalc-x.x-aarch64.app              | portable unsigned App file for macOS on Apple Silicon Processors |
| prakticalc-x.x.tcz*                     | PraktiCalc TinyCore Extension, can be loaded on TinyCore 17+     |
| Source code (zip)                       | ZIP archive with the source code                                 |
| Source code (tar.gz)                    | gzipped tar archive with the source code                         |

Please note that the macOS package is unsigned. Look up how to open unsigned Apps on macOS to use it.

#### Building PraktiCalc
The build scripts will help you to build PraktiCalc into installable packages.
For building on Windows 10 or newer, you need Python with tkinter and the following modules installed via pip: ```ttkthemes```, ```pyinstaller```
For older versions of Windows, you need Python with the same modules and PowerShell 5 or 7-Zip installed. The lastest available Python version is recommended, that being Python 3.8.20 on Windows NT 6 (Windows 7/Vista). Windows Vista is unsupported by PraktiCalc, but should work in theory.
Buildung deb packages required the following dependencies installed via apt from the Debian package sources: ```python3-tk```, ```python3-ttkthemes```. AppImages require the same packages and additionally ```python3-pyinstaller```. ```appimagetool``` will be downloaded automatically by the build script. AppImageUpdate is also supported, by the way.
