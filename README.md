# PraktiCalc
A practical calculator with GUI featuring a calculating history, an extension system & UI theming, as well as integration for many dialog tools.
<img alt="PraktiCalc Screenshot" src="https://raw.githubusercontent.com/karl152/PraktiCalcScreenshots/refs/heads/main/PraktiCalc1.5.png"/>
*Screenshot of PraktiCalc 1.5*

## Features
### Calculation
PraktiCalc contains all basic operators you know, it also has square roots, parenthesis, modulo, factorial, trigonometry and hyperbolic functions.<br>
It also lets you type in your entire calculation and only calculates when you press <kbd>=</kbd>/<kbd>Enter</kbd>. You can also work on from your previous result.<br>
The memory system allows you to keep numbers and add, subtract, append, set, get, and delete.

<img width="582" height="638" alt="Main window" src="https://github.com/user-attachments/assets/7d4698f8-c0b9-4543-8044-a92c37df6247"/>

*The main window*

### Keyboard Input
Almost all buttons are mapped to keys, so you can just type on your keyboard instead of pressing all the buttons with your mouse.
#### Keyboard shortcuts
<table>
    <tr>
        <th>Key</th>
        <th>Action</th>
    </tr>
    <tr>
        <td><kbd>H</kbd></td>
        <td>opens the calculation history</td>
    </tr>
    <tr>
        <td><kbd>S</kbd></td>
        <td>opens the settings menu</td>
    </tr>
    <tr>
        <td><kbd>X</kbd></td>
        <td>opens the extension window</td>
    </tr>
        <tr>
        <td><kbd>I</kbd></td>
        <td>opens the about dialog</td>
    </tr>
    <tr>
        <td><kbd>M</kbd></td>
        <td>shows the memory menu</td>
    </tr>
    <tr>
        <td><kbd>Q</kbd></td>
        <td>closes PraktiCalc</td>
    </tr>
    <tr>
        <td><kbd>Return</kbd></td>
        <td>calculates the given input</td>
    </tr>
    <tr>
        <td><kbd>Backspace</kbd></td>
        <td>removed the last character from the input</td>
    </tr>
</table>

Keys that just append a character:
* <kbd>0</kbd>-<kbd>9</kbd>, <kbd>+</kbd>, <kbd>-</kbd>, <kbd>*</kbd>, <kbd>/</kbd>, <kbd>%</kbd>, <kbd>(</kbd>, <kbd>)</kbd>, <kbd>e</kbd>, <kbd>.</kbd>, <kbd>,</kbd>, <kbd>!</kbd>
> [!NOTE]
> <kbd>%</kbd> is the modulo operator in this case, not a percent sign. You won't be able to calculate a percentage into a decimal number, use "/100" instead.

### Configurable Behavior
In the behavior settings, you can choose what angle unit you want to use, and change other preferences.

<img width="360" height="528" alt="Settings window" src="https://github.com/user-attachments/assets/abe5943f-4cef-468f-a731-79ee10641362" />

*The settings window with the behavior tab open*

### Calculation History
PraktiCalc saves all successful calculations in the history until you close the program. You can also clear the history if you want.

<img width="394" height="444" alt="History window" src="https://github.com/user-attachments/assets/bb9a4978-a9bc-4bf2-a8f5-403b54766c07" />

*The calculation history window*

### Customizable UI
On Windows and macOS, PraktiCalc trys to look like the operating system. However, with the power of [ttk](https://wiki.tcl-lang.org/page/Ttk) and [ttkthemes](https://github.com/TkinterEP/ttkthemes), there are many themes to choose from.<br>
Not all available themes are shown in the selection by far, you can get a complete list of themes included in ttkthemes [here](https://ttkthemes.readthedocs.io/en/latest/themes.html).

<img width="582" height="638" alt="Some UI themes" src="https://github.com/user-attachments/assets/1d842ed7-3453-4462-82c2-f9ba88ae8738" />

*Some themes from ttkthemes that are right available from the settings window*

Changing the theme is not the only thing you can do - you can even choose between different menu bars or even use your window title bar as the calculator display!

<img width="582" height="638" alt="PraktiCalc using it's window title as a display" src="https://github.com/user-attachments/assets/26631ef3-2ad6-456f-b093-c24c11558a61" />
<img width="360" height="528" alt="Appearance tab in the settings" src="https://github.com/user-attachments/assets/51a296d8-22d9-4cc3-a1e7-86c1cb9c2c3c" />

*Using the window title bar as the calculator display*

### Support for many dialog tools
How many designs do you need for the dialogs? One? PraktiCalc has way more. Introducing the division by zero error dialog gallery :)

<img width="262" height="228" alt="VBScript" src="https://github.com/user-attachments/assets/2522f639-4332-4d00-97b8-9ce2ab2ab3cf" />
<img width="317" height="180" alt="Alternative (Windows)" src="https://github.com/user-attachments/assets/50354444-9547-4d6a-b9fe-81dd2207bb76" />
<img width="261" height="251" alt="TkInter (Windows)" src="https://github.com/user-attachments/assets/84928518-5504-4f1a-a8e3-127f132ae268" />
<img width="959" height="244" alt="notify-send" src="https://github.com/user-attachments/assets/75d5e07f-6d1c-46ac-bdfa-a8b6ed670265" />
<img width="600" height="444" alt="zenity" src="https://github.com/user-attachments/assets/79a7048a-b8b5-4622-b637-7366341fe506" />
<img width="426" height="256" alt="kdialog" src="https://github.com/user-attachments/assets/0570d15b-679c-4c48-95f3-c4c81fbe90d4" />
<img width="370" height="234" alt="yad" src="https://github.com/user-attachments/assets/910b1150-841a-44f4-887d-726d06c265b2" />
<img width="420" height="288" alt="gxmessage" src="https://github.com/user-attachments/assets/225447ec-697a-4172-83e8-43e8fa6f58d2" />
<img width="261" height="112" alt="xmessage" src="https://github.com/user-attachments/assets/f1c75702-0b57-41db-8189-ae00a4fa7b17" />
<img width="419" height="221" alt="Alternative (Linux)" src="https://github.com/user-attachments/assets/c6badafa-bdf5-4c94-a71e-9bf7824bee2c" />
<img width="337" height="202" alt="TkInter (Linux)" src="https://github.com/user-attachments/assets/4036eb99-3b3c-4d9a-b92a-56e085581157" />
<br>
These aren't all by the way.

### The Extension System
PraktiCalc has its own extension system, currently working with the PraktiXtension format. More information can be found at the end of this file or at these sites:
* [PraktiXtension Gallery](https://praktixtensions.blogspot.com/)
* [PraktiXtension Docs (at the gallery)](https://praktixtensions.blogspot.com/p/docs.html)
* [PraktiXtension Docs (on GitHub)](https://github.com/karl152/PraktiXtensions/blob/main/README.md)
* [PraktiXtension GitHub](https://github.com/karl152/PraktiXtensions)
* [Submit your PraktiXtension](https://praktixtensions.blogspot.com/p/submit.html)
* [Download the PXT Builder extension](https://raw.githubusercontent.com/karl152/PraktiXtensions/refs/heads/main/PXTBuilder.pxt)

There are some preinstalled extensions included and updated within PraktiCalc:
#### Decimal Converter
This extension converts decimal numbers into binary and hexadecimal numbers. It was a standalone feature until PraktiCalc 1.4 and was converted into an extension for PraktiCalc 1.5.

<img width="1632" height="1221" alt="Decimal Converter" src="https://github.com/user-attachments/assets/11502fee-0cc0-4414-be2e-7cecec58ecb1" />

*The Decimal Converter*

#### PraktiGraph
PraktiGraph draws graphs from given functions in different colors. It also features a zoom and a small value table.

<img width="1632" height="1221" alt="PraktiGraph" src="https://github.com/user-attachments/assets/44d469a4-a3ae-4551-90dc-f49f73a830a2" />

*PraktiGraph.*

#### Extension Manager
Installing and managing extensions was a bit difficult, so I made an extension manager which provides a graphical user interface for managing extensions and viewing metadata.
It is essentially an extension to manage extensions, so you could also use the extension manager to uninstall itself, I wouldn't recommend doing that though.

<img width="1632" height="1221" alt="Extension Manager" src="https://github.com/user-attachments/assets/6f1b768f-8cb3-4c9d-90cc-b83ba1b14223" />

*The extension manager managing extensions*

### Support for Windows 7
I don't use Windows 7 actively anymore for security reasons, but I still support it.

<img width="1920" height="1080" alt="PraktiCalc on Windows Home Server 2011" src="https://github.com/user-attachments/assets/78829a54-277d-4bd3-9b77-bd3b7fb05a6c" />

*PraktiCalc running perfectly fine on Windows 7. Actually is Windows Home Server 2011, I don't have my main Windows 7 machine right now*

### ...many more
Listing all the features here would take far too long, and almost nobody would read it anyways, you'll find out about the other features sooner or later when using PraktiCalc yourself.<br>
Just give it a try and download it, it's available for many platforms.

## Get PraktiCalc
You can download PraktiCalc at the [Releases page](https://github.com/karl152/PraktiCalc/releases) on GitHub. There should be a few files for each release there:
<table>
    <tr>
        <th>File name example</th>
        <th>Description</th>
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
        <th>Operating system</th>
        <th>Build script</th>
        <th>Dependencies</th>
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
