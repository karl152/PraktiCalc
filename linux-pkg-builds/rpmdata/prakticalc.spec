Name:		prakticalc
Version:		1.5.2
Release:		1%{?dist}
Summary:	practical calculator written in Python

License:		GPL-3.0-only
Source0:		%{name}.tar.gz

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
