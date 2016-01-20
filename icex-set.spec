Name:		icex-set
Version:	0.0.1
Release:	alt1
Summary:	Graphical icewm settings

License:	GPL
Group:		Graphical desktop/Icewm
URL:		https://github.com/150balbes/icex-set
Packager:	Oleg Ivanov <Leo-sp150@yandex.ru>

Source0:	%name-%version.tar.gz
Source2:	%name.desktop
Source3:	%name.png
###Source4:	%name.d.tar

BuildRequires: gcc-c++ libqt4-devel desktop-file-utils
Requires: qt4-styles-qtcurve

%description
Graphical application for Icewm

%prep
%setup -q
lrelease-qt4 %name.pro
DESTDIR=%buildroot PREFIX=/usr qmake-qt4 %name.pro

%build
%make_build

%install
%makeinstall
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -pD -m644 %SOURCE3 %buildroot%_liconsdir/%name.png

%files
%_bindir/%name
%_desktopdir/*
%_liconsdir/*

%changelog
* Tue Jan 19 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt1
- Initial release
