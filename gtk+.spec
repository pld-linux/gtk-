Summary:	The Gimp Toolkit
Summary(cs):	Sada nástrojù pro Gimp
Summary(de):	Der Gimp-Toolkit
Summary(fi):	Gimp-työkalukokoelma
Summary(fr):	Le toolkit de Gimp.
Summary(it):	Il toolkit per Gimp
Summary(pl):	Gimp Toolkit
Summary(tr):	Gimp ToolKit arayüz kitaplýðý
Name:		gtk+
Version:	1.2.8
Release:	2
License:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gimp.org/pub/GNOME/stable/latest/sources/%{name}-%{version}.tar.gz
Patch0:		gtk+-info.patch
Patch1:		gtk+-ahiguti.patch
URL:		http://www.gtk.org/
Icon:		gtk+.xpm
Requires:	glib >= %{version}
Requires:	iconv
BuildRequires:	glib-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_infodir	/usr/share/info
%define		_mandir		/usr/X11R6/man
%define		_sysconfdir	%{_datadir}

%description
Gtk+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to be
small, efficient, and flexible. Gtk+ is written in C with a very
object-oriented approach. Gdk (part of Gtk+) is a drawing toolkit which
provides a thin layer over Xlib to help automate things like dealing with
different color depths, and Gtk is a widget set for creating user
interfaces.

%description -l cs
Knihovny X pùvodnì psané pro GIMP, které nyní pou¾ívá také øada jiných
programù.

%description -l da
X biblioteker, oprindeligt udviklet til GIMP, men anvendes nu af flere
forskellige programmer.

%description -l de
Die X-Libraries, die ursprünglich für GIMP geschrieben wurden und
mittlerweile für eine ganze Reihe anderer Programme benutzt werden.

%description -l fr
X-kirjastot, jotka alunperin kirjoitettiin GIMP:lle, mutta joita käytetään
nyt myös useissa muissakin ohjelmissa.

%description -l it
Libreria X scritta per GIMP. Viene usata da diversi programmi.

%description -l pl
Gtk+, która to biblioteka sta³a siê podstaw± programu Gimp zawiera funkcje
do tworzenia graficznego interfrjsu uzytkownika pod X Window. By³a tworzona
z za³o¿eniem ¿eby by³a ma³a, efektywna i wygodna. Gtk+ jest napiane w C z
podej¶ciem zorientowanym bardzo obiektowo. Gdk (czê¶æ Gtk+) jest warsw±
po¶redni± pomiêdzy Xlib i reszt± toolkit zapewniaj±c± pracê niezale¿nie od
g³êbi koloru (ilo¶ci bitów na piksel). Gtk (druga czê¶æ Gtk+) jest
natomiast ju¿ zbiorem ró¿nego rodzaju kontrolek s³u¿±cych do tworzenia
interfejsu u¿ytkownika.

%description -l tr
Baþlangýçta GIMP için yazýlmýþ X kitaplýklarý. Þu anda baþka programlarca
da kullanýlmaktadýr.

%package devel
Summary:	Gtk+ header files and development documentation
Summary(cs):	Sada nástrojù GIMP a kreslící kit GIMP
Summary(da):	GIMP Toolkit og GIMP Tegnings-værktøj
Summary(de):	GIMP Toolkit und GIMP Drawing Kit
Summary(fi):	Gimp-työkalukokoelma ja Gimp-piirtotyökalut
Summary(fr):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK).
Summary(it):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl):	Pliki nag³ówkowe i dokumentacja do Gtk+ 
Summary(tr):	GIMP araç takýmý ve çizim takýmý
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	glib-devel >= %{version}
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	libtool  >= 1.3.2
# Every program using gtk+ should get a list of libraries to link with by
# executing `gtk-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with gtk+.
Requires:	XFree86-devel
Requires:	glib-devel

%description devel
Header files and development documentation for the Gtk+ libraries.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do bibliotek Gtk+.

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
%setup  -q
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-debug=no \
	--enable-shm

%{__make} m4datadir=/usr/share/aclocal

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines

%{__make} install \
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
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755) 
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%lang(bg) %{_sysconfdir}/gtk/gtkrc.bg*
%lang(cs) %{_sysconfdir}/gtk/gtkrc.cs
%lang(cy) %{_sysconfdir}/gtk/gtkrc.cy
%lang(el) %{_sysconfdir}/gtk/gtkrc.el
%lang(eo) %{_sysconfdir}/gtk/gtkrc.eo
%lang(et) %{_sysconfdir}/gtk/gtkrc.et
%lang(ga) %{_sysconfdir}/gtk/gtkrc.ga
%lang(he) %{_sysconfdir}/gtk/gtkrc.he
%lang(hr) %{_sysconfdir}/gtk/gtkrc.hr
%lang(hu) %{_sysconfdir}/gtk/gtkrc.hu
%lang(hy) %{_sysconfdir}/gtk/gtkrc.hy
%lang(ja) %{_sysconfdir}/gtk/gtkrc.ja
%lang(ka) %{_sysconfdir}/gtk/gtkrc.ka*
%lang(ko) %{_sysconfdir}/gtk/gtkrc.ko
%lang(lt) %{_sysconfdir}/gtk/gtkrc.lt
%lang(mk) %{_sysconfdir}/gtk/gtkrc.mk
%lang(pl) %{_sysconfdir}/gtk/gtkrc.pl
%lang(ro) %{_sysconfdir}/gtk/gtkrc.ro
%lang(ru) %{_sysconfdir}/gtk/gtkrc.ru*
%lang(sk) %{_sysconfdir}/gtk/gtkrc.sk
%lang(sl) %{_sysconfdir}/gtk/gtkrc.sl
%lang(sq) %{_sysconfdir}/gtk/gtkrc.sq
%lang(sr) %{_sysconfdir}/gtk/gtkrc.sr
%lang(th) %{_sysconfdir}/gtk/gtkrc.th
%lang(tr) %{_sysconfdir}/gtk/gtkrc.tr
%lang(uk) %{_sysconfdir}/gtk/gtkrc.uk
%lang(vi) %{_sysconfdir}/gtk/gtkrc.vi*
%lang(zh) %{_sysconfdir}/gtk/gtkrc.zh*
%lang(cs,hr,hu,pl,ro,sk,sl,sq) %{_sysconfdir}/gtk/gtkrc.iso-8859-2
%lang(bg,mk,ru,sr) %{_sysconfdir}/gtk/gtkrc.iso-8859-5
%lang(lt) %{_sysconfdir}/gtk/gtkrc.iso-8859-13
%lang(cy,ga) %{_sysconfdir}/gtk/gtkrc.iso-8859-14
%lang(et) %{_sysconfdir}/gtk/gtkrc.iso-8859-15

%dir %{_libdir}/gtk/themes
%dir %{_libdir}/gtk/themes/engines
%dir %{_datadir}/themes

%{_datadir}/themes/Default

%files devel
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/*

%{_includedir}/*
%{_infodir}/*info*gz
/usr/share/aclocal/*.m4

%{_mandir}/man1/gtk-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
