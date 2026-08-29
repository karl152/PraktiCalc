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
        <td>TinyCore extension, compatible with Tiny Core 17 and newer</td>
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

> [!IMPORTANT]
> The macOS builds are unsigned and won't work thanks to Gatekeeper. Open them with right click the first time as a workaround.

#### Distributions & Mirrors
There are two PPAs for Ubuntu and Ubuntu-based systems, which you can enable to get automatic updates for PraktiCalc. The [karl52/prakticalc](https://launchpad.net/~karl52/+archive/ubuntu/prakticalc) PPA always tracks the latest release, while the [karl52/prakticalc-lts](https://launchpad.net/~karl52/+archive/ubuntu/prakticalc-lts) PPA always tracks the latest 1.5.x release. You can install PPAs by running `sudo add-apt-repository ppa:karl52/prakticalc`.

There are two git mirrors, one on [SourceForge](https://sourceforge.net/p/prakticalc/code/) and one on [Launchpad](https://git.launchpad.net/~karl52/+git/PraktiCalc)

### Building PraktiCalc
Generally, you need Python 3.8 or newer with TkInter (Tcl/Tk). These build scripts will help you to build PraktiCalc into installable packages.

<table>
    <tr>
        <th>operating system</th>
        <th>build script</th>
        <th>dependencies</th>
    </tr>
    <tr>
        <td>Windows</td>
        <td>windows_build.ps1</td>
        <td>tkinter, pyinstaller, ttkthemes; PowerShell 5+ or PowerShell 2+ with 7-Zip</td>
    </tr>
    <tr>
        <td>macOS</td>
        <td>macos-build.applescript</td>
        <td>Xcode Command Line Tools, modern Python (not the one from Xcode) with tkinter, ttkthemes and pyinstaller</td>
    </tr>
    <tr>
        <td>Linux AppImage</td>
        <td>appimage_build.sh</td>
        <td>wget2/wget/curl; Python with tkinter, ttkthemes, pyinstaller; build system must be able to run AppImages</td>
    </tr>
    <tr>
        <td>Debian (only deb)</td>
        <td>debian_build.sh</td>
        <td>dash, gzip, nano, dpkg-deb, optional lintian</td>
    </tr>
    <tr>
        <td>Debian (deb & dsc)</td>
        <td>deb-dsc-build.sh</td>
        <td>dash, gzip, dh, dpkg-buildpackage</td>
    </tr>
    <tr>
        <td>Fedora Linux</td>
        <td>rpm-build.sh</td>
        <td>rpm-build, rpmdevtools, python3-tkinter, python3-devel</td>
    </tr>
    <tr>
        <td>Tiny Core Linux</td>
        <td>tinycore.build.sh</td>
        <td>squashfs-tools</td>
    </tr>
</table>

> [!NOTE]
> While `ttkthemes` is highly recommended, PraktiCalc also works without it.

### Extension system
PraktiXtensions are Python scripts that add a tab with a TkInter GUI to the extension window. They can use any modules imported in the main file. For the graphical user interface, ttk widgets should be used. If that's not possible, consider using the value of the `DarkMode` parameter to set the background and foreground colors.
A full extension has three files: the Python file with the code itself, a metadata file and a description. These metadata entries will be shown by the built-in extension manager. You can distribute your extensions as a single PXT file, which is basically a renamed ZIP archive.
Consider using the [PXT Builder](https://raw.githubusercontent.com/karl152/PraktiXtensions/refs/heads/main/PXTBuilder.pxt) (which is an extension itself) for comfortably building PXT files from Python files.

More documentation is available at https://github.com/karl152/PraktiXtensions. Also check out the [PraktiXtension Gallery](https://praktixtensions.blogspot.com/).
