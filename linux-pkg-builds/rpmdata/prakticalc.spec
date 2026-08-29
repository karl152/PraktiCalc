Name:		prakticalc
Version:	1.5.6
Release:	1%{?dist}
Summary:	practical calculator written in Python

License:	GPL-3.0-only
Source0:	%{name}.tar.gz

BuildArch:	noarch

Requires:	python3
Requires:	python3-tkinter

%description
A practical calculator written in Python with Tkinter and TTK

%prep
%setup -q -n %{name}

%build
# nothing to build

%install
cp -r * %{buildroot}/

%files
/usr/bin/prakticalc
/usr/share/prakticalc
/usr/share/applications
/usr/share/metainfo
/usr/share/icons
/usr/share/man

%license usr/share/prakticalc/LICENSE

%changelog
* Sat Aug 29 2026 Karl Wesseler <karldpbkz@gmail.com> - 1.5.6
- Added Q keybind to close the main window
- Reworked README.md
- Improved unicode superscript support in PraktiGraph
- Slightly improved UI code by making both menu bars use the same menus
- Fixed a bunch of issues with PraktiGraph
- Fixed failed extension calculations staying in the calculator
- Added M keybind with floating memory menu in 1.5.5 (forgot to mention that)
* Fri Aug 28 2026 Karl Wesseler <karldpbkz@gmail.com> - 1.5.5
- added the ability to omit * in PraktiGraph
- added patch for deb-dsc-build.sh for Ubuntu 20.04 PPAs
- added accelerator labels to menus
- added line break to settings reset message
- ajusted default theming settings
- improved error detection for uninstallations on Windows
- improved configuration management
- improved focus handling for windows and widgets
- improved extension reinstalling/upgrading
- slightly improved the sidebar in Extension Manager
- changed console font to be fixed-width on all systems
- fixed stretched Linux icons
- fixed "0" turning into "" when pressing backspace
* Fri Aug 21 2026 Karl Wesseler <karldpbkz@gmail.com> - 1.5.4
- updated to Tk 9.0 for Windows 11 builds
- restructured the info dialog
- added highlights to exit buttons in alternative dialogs
- added keybinds "C", ".", "%", "!"
- added number of files to progressbar in Windows installer (Tk 9.0 only)
- allowed for new calculations to be started with 0
- improved Decimal Converter by adding scrollbars and using capital letters
- re-enabled input focus on Windows in Decimal Converter
- cleaned up some UI code
- improved macOS build script and fixed the application name and info dialog
- added dependence checking in build scripts for macOS and Windows
- removed "feel free to close this window" state in extension window
- fixed calculation string getting replaced under certain circumstances
- fixed settings window hiding after displaying restart messagebox
- fixed AppImage build script not fully restoring its directory after build
- fixed info dialog not closing when pressing the enter key
- fixed keybinds for Tk 9.0
- fixed the Windows icon being stretched
- fixed ttk theming without ttkthemes on Windows
* Sat Aug 01 2026 Karl Wesseler <karldpbkz@gmail.com> - 1.5.3
- Added a button to open the extension folder from extension manager
- Added a scrollbar to the extension manager
- The "E" key now types e (euler's number)
- Decreased installation size on Windows by about 30%
- Enabled word wrapping for long descriptions in extension manager
- Made header text in the extension manager shorter
- Removed downgrading support in Windows installer
- Improved memory system
- Improved error dialogs: xmessage, gxmessage, wmessage, notify-send
- More user feedback when installing extensions or resetting the settings
- Better error handling in the extension window
- Improved the build system
- Disabled Modify and Repair in Programs and Features on Windows
- Fixed licenses not shown in extension manager in metadata is missing
- Fixed extension window size on Fedora
* Sun Jul 12 2026 Karl Wesseler <karldpbkz@gmail.com> - 1.5.2
- Added Fedora RPM builds
- Added new Debian package build system with source package support
- Reworked theming to work without ttkthemes
- Added "clam" and "alt" ttk themes to settings menu
- Added memory append, add and subtract operations
- Improved DPI scaling and accuracy in PraktiGraph
- Added unicode superscript support in PraktiGraph
- added a link to the PraktiXtension gallery in Extension Manager
- descriptions now use fixed-width font and a scrollbar in Extension Manager
- file open dialogs now start in the user's home directory in Extension Manager
- the used version of Tk is now shown in the info dialog
- if VBS is used, the VBScript version is shown as well in the info dialog
- the info dialog only mentions ttkthemes if it's actually in use
- some Tk bitmaps are shown in the info dialog if debug mode is activated
- AppleScript dialogs now have window titles
- Pressing "X" now opens the extension window
* Fri May 29 2026 Karl "karl152" <karldpbkz@gmail.com> - 1.5
- Initial RPM release
