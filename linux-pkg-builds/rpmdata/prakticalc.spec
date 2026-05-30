Name:		prakticalc
Version:		1.5.1
Release:		1%{?dist}
Summary:	practical calculator written in Python

License:		GPL-3
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
* Fri May 29 2026 Karl "karl152" <karldpbkz@gmail.com> - 1.5
- Initial RPM release
