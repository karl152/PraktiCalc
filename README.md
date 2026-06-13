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
| prakticalc-x.x-win-amd64-portable.zip   | PraktiCalc for Windows 11 on 64-Bit x86 Processors (Portable)    |
| prakticalc-x.x-win7-amd64-portable.zip  | PraktiCalc for Windows 7+ on 64-Bit x86 Processors (Portable)    |
| prakticalc-x.x.deb                      | installable PraktiCalc Debian Package                            |
| prakticalc-x.x-amd64.AppImage           | portable AppImage file for Linux on 64-Bit x86 Processors        |
| prakticalc-x.x-aarch64.AppImage         | portable AppImage file for Linux on 64-Bit ARM Processors        |
| prakticalc-x.x-aarch64.app              | portable unsigned App file for macOS on Apple Silicon Processors |
| prakticalc-x.x.tcz*                     | PraktiCalc TinyCore Extension, can be loaded on TinyCore 17+     |
| peakticalc-x.x.rpm                      | installable PraktiCalc Fedora RPM package                        |
| Source code (zip)                       | ZIP archive with the source code                                 |
| Source code (tar.gz)                    | gzipped tar archive with the source code                         |

Please note that the macOS package is unsigned. Look up how to open unsigned Apps on macOS to use it.

#### Building PraktiCalc
The build scripts will help you to build PraktiCalc into installable packages.
For building on Windows 10 or newer, you need Python with tkinter and the following modules installed via pip: ```ttkthemes```, ```pyinstaller```
For older versions of Windows, you need Python with the same modules and PowerShell 5 or 7-Zip installed. The lastest available Python version is recommended, that being Python 3.8.20 on Windows NT 6 (Windows 7/Vista). Windows Vista is unsupported by PraktiCalc, but should work in theory.
Buildung deb packages required the following dependencies installed via apt from the Debian package sources: ```python3-tk```, ```python3-ttkthemes```. AppImages require the same packages and additionally ```python3-pyinstaller```. ```appimagetool``` will be downloaded automatically by the build script. AppImageUpdate is also supported, by the way. RPMs need `rpm-build`, `rpmdevtools`, `python3-devel` and `python3-tkinter`.

#### Extension system
PraktiXtensions are Python scripts that add a tab with a TkInter-GUI to the extension window. They can use any modules imported in the main file. For the graphical user interface, ttk-Widgets should be used. If that's not possible, consider using the value of the DarkMode parameter to set the background and foreground colors.
A full extension has three files: the Python file with the code itself, a metadata file and a description. These metadata entries will be shown by the built-in extension manager. You can distribute your extensions as a single PXT file, which is basically a renamed ZIP archive.
Consider using the [PXT Builder](https://github.com/user-attachments/files/27288923/PXTBuilder.zip) (which is an extension itself) for comfortably building PXT files from Python files.
More documentation will be available at some point at https://github.com/karl152/PraktiXtensions
