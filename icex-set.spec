Name:		icex-set
Version:	0.0.2
Release:	alt1
Summary:	Graphical icewm settings

License:	GPL
Group:		Graphical desktop/Icewm
URL:		https://github.com/150balbes/icex-set
Packager:	Oleg Ivanov <Leo-sp150@yandex.ru>

Source0:	%name-%version.tar.gz
Source2:	%name.desktop
Source3:	%name.png
Source4:	1000.jpg

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
mkdir -p %buildroot%_datadir/wallpapers
install -pD -m644 %SOURCE4 %buildroot%_datadir/wallpapers/1000.jpg


%files
%_bindir/%name
%_desktopdir/*
%_liconsdir/*
%_datadir/wallpapers/*

%changelog
* Tue Mar 09 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.2-alt1
- new ver

* Tue Jan 23 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt5
- edit icex-set.png

* Tue Jan 23 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt4
- add preview image

* Tue Jan 19 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt3
- edit

* Tue Jan 19 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt1
- Initial release
