Summary:	The Gimp Toolkit
Summary(pl):	Gimp Toolkit
Name:		gtk+
Version:	1.2.4
Release:	1
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gimp.org/pub/gtk/v1.1/%{name}-%{version}.tar.gz
Patch0:		gtk+-info.patch
URL:		http://www.gtk.org/
Icon:		gtk+.gif
Requires:	glib = %{version}
BuildRequires:	glib-devel = %{version}
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_infodir	/usr/share/info
%define		_mandir		/usr/X11R6/man
%define		_sysconfdir	/etc/X11

%description
Gtk+, which stands for the Gimp ToolKit, is a library for creating graphical
user interfaces for the X Window System. It is designed to be small,
efficient, and flexible. Gtk+ is written in C with a very object-oriented
approach.
Gdk (part of Gtk+) is a drawing toolkit which provides a thin layer over
Xlib to help automate things like dealing with different color depths, and
Gtk is a widget set for creating user interfaces.

%description -l pl
Gtk+, kt�tra to biblioteka sta�a si� podstaw� programu Gimp zawiera funkcje
do tworzenia graficznego interfrjsu uzytkownika pod X Window. By�a tworzona
z za�o�eniem �eby bya ma�a, efektywna i wygodna. Gtk+ jest napiane w C z
podej�ciem zorientowanym bardzo obiektowo.
Gdk (cz�� Gtk+) jest warsw� po�redni� pomi�dzy Xlib i reszt� toolkit
zapewniaj�c� prac� niezale�nie od g��bi koloru (ilo�ci bit�w na piksel).
Gtk (druga cz�� Gtk+) jest natomiast ju� zbiorem r�nego rodzaju kontrolek
s�u��cych do tworzenia interfejsu u�ytkownika.

%package devel
Summary:	Gtk+ header files and development documentation
Summary(pl):	Pliki nag��wkowe i dokumentacja do Gtk+ 
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
PreReq:		/sbin/install-info
Requires:	%{name} = %{version}
Requires:	glib-devel = %{version}
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	libtool  >= 1.3.2

%description devel
Header files and development documentation for the Gtk+ libraries.

%description -l pl devel
Pliki nag��wkowe i dokumentacja do bibliotek Gtk+.

%package static
Summary:	Gtk+ static libraries
Summary(pl):	Biblioteki statyczne Gtk+
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Gtk+ static libraries.

%description -l pl static
Biblioteki statyczne Gtk+

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-debug=no \
	--enable-shm

make m4datadir=/usr/share/aclocal

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=/usr/share/aclocal \
	gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9n $RPM_BUILD_ROOT{%{_infodir}/*info*,%{_mandir}/man1/*} \
	AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/gdk.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/gtk.info.gz /etc/info-dir

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/gdk.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/gtk.info.gz /etc/info-dir
fi

%files -f %{name}.lang
%defattr(644,root,root,755) 
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%lang(cs) %{_sysconfdir}/gtk/gtkrc.cs
%lang(hr) %{_sysconfdir}/gtk/gtkrc.hr
%lang(hu) %{_sysconfdir}/gtk/gtkrc.hu
%lang(ja) %{_sysconfdir}/gtk/gtkrc.ja
%lang(ko) %{_sysconfdir}/gtk/gtkrc.ko
%lang(pl) %{_sysconfdir}/gtk/gtkrc.pl
%lang(ru) %{_sysconfdir}/gtk/gtkrc.ru
%lang(sk) %{_sysconfdir}/gtk/gtkrc.sk
%lang(sl) %{_sysconfdir}/gtk/gtkrc.sl
%lang(cs,hr,hu,pl,sk,sl) %{_sysconfdir}/gtk/gtkrc.iso-8859-2

%dir %{_libdir}/gtk/themes
%dir %{_libdir}/gtk/themes/engines
%dir %{_datadir}/themes

%{_datadir}/themes/Default

%files devel
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/*

%{_includedir}/*
%{_infodir}/*info*gz
/usr/share/aclocal/*.m4

%{_mandir}/man1/gtk-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
