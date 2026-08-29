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
You can download PraktiCalc at the [Releases page](https://github.com/karl152/PraktiCalc/releases) on GitHub. There should be a few files for each release there:
<table>
    <tr>
        <th>file name example</th>
        <th>description</th>
    </tr>
    <tr>
        <td>prakticalc-x.x-win-amd64-installer.exe</td>
        <td>Installer for Windows 11 on AMD64</td>
    </tr>
    <tr>
        <td>prakticalc-x.x-win-amd64-portable.exe</td>
        <td>Portable executable for Windows 11 on AMD64</td>
    </tr>
    <tr>
        <td>prakticalc-x.x-win7-amd64-installer.exe</td>
        <td>Installer for Windows 7 on AMD64</td>
    </tr>
    <tr>
        <td>prakticalc-x.x-win7-amd64-portable.exe</td>
        <td>Portable executable for Windows 7 on AMD64</td>
    </tr>
    <tr>
        <td>prakticalc-x.x-aarch64.app.zip</td>
        <td>Zipped unsigned app folder for macOS on Apple Silicon</td>
    </tr>
    <tr>
        <td>prakticalc-x.x.deb</td>
        <td>Package for Debian stable</td>
    </tr>
    <tr>
        <td>prakticalc-x.x-x.fcxx.noarch.rpm</td>
        <td>RPM package for the latest Fedora Linux</td>
    </tr>
    <tr>
        <td>prakticalc-x.x.tcz*</td>
        <td>TinyCore extension, compatible with TinyCore 17 and newer</td>
    </tr>
    <tr>
        <td>PraktiCalc-x86_64.AppImage</td>
        <td>Linux AppImage for AMD64 processors (built on Debian stable)</td>
    </tr>
    <tr>
        <td>PraktiCalc-aarch64.AppImage</td>
        <td>Linux AppImage for ARM64 processors (built on Debian stable)</td>
    </tr>
    <tr>
        <td>Source code (zip)</td>
        <td>ZIP archive with the source code</td>
    </tr>
    <tr>
        <td>Source code (tar.gz)</td>
        <td>Gzipped tar archive with the source code</td>
    </tr>
</table>

Please note that the macOS package is unsigned. Look up how to open unsigned Apps on macOS to use it.

#### Building PraktiCalc
The build scripts will help you to build PraktiCalc into installable packages.
For building on Windows 10 or newer, you need Python with tkinter and the following modules installed via pip: `ttkthemes`, `pyinstaller`
For older versions of Windows, you need Python with the same modules and PowerShell 5 or 7-Zip installed. The lastest available Python version is recommended, that being Python 3.8.20 on Windows NT 6 (Windows 7/Vista). Windows Vista is unsupported by PraktiCalc, but should work in theory.
Buildung deb packages required the following dependencies installed via apt from the Debian package sources: `python3-tk`, `python3-ttkthemes`. AppImages require the same packages and additionally `python3-pyinstaller`. `appimagetool` will be downloaded automatically by the build script. AppImageUpdate is also supported, by the way. RPMs need `rpm-build`, `rpmdevtools`, `python3-devel` and `python3-tkinter`.

#### Extension system
PraktiXtensions are Python scripts that add a tab with a TkInter-GUI to the extension window. They can use any modules imported in the main file. For the graphical user interface, ttk-Widgets should be used. If that's not possible, consider using the value of the DarkMode parameter to set the background and foreground colors.
A full extension has three files: the Python file with the code itself, a metadata file and a description. These metadata entries will be shown by the built-in extension manager. You can distribute your extensions as a single PXT file, which is basically a renamed ZIP archive.
Consider using the [PXT Builder](https://raw.githubusercontent.com/karl152/PraktiXtensions/refs/heads/main/PXTBuilder.pxt) (which is an extension itself) for comfortably building PXT files from Python files.

More documentation is available at https://github.com/karl152/PraktiXtensions. Also check out the [extension gallery](https://praktixtensions.blogspot.com/)
