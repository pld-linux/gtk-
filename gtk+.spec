Summary:	The Gimp Toolkit
Summary(cs):	Sada nástrojù pro Gimp
Summary(de):	Der Gimp-Toolkit
Summary(es):	Conjunto de herramientas Gimp
Summary(fi):	Gimp-työkalukokoelma
Summary(fr):	Le toolkit de Gimp
Summary(it):	Il toolkit per Gimp
Summary(pl):	Gimp Toolkit
Summary(pt_BR):	Kit de ferramentas Gimp
Summary(tr):	Gimp ToolKit arayüz kitaplýðý
Name:		gtk+
Version:	1.2.10
Release:	7
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.2/%{name}-%{version}.tar.gz
Source1:	http://developer.gnome.org/doc/API/gdk-docs.tar.gz
Source2:	http://developer.gnome.org/doc/API/gtk-docs.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-ahiguti.patch
Patch2:		%{name}-strip.patch
Patch3:		%{name}-pkgconfig.patch
Patch4:		%{name}-focus.patch
URL:		http://www.gtk.org/
Icon:		gtk+.xpm
Requires:	glib >= %{version}
Requires:	iconv
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= %{version}
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtk+1.2

%define		_prefix		/usr/X11R6
%define		_infodir	/usr/share/info
%define		_mandir		/usr/X11R6/man
%define		_sysconfdir	%{_datadir}

%description
Gtk+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. Gtk+ is written in C with a very
object-oriented approach. Gdk (part of Gtk+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and Gtk is a widget set for
creating user interfaces.

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
X-kirjastot, jotka alunperin kirjoitettiin GIMP:lle, mutta joita
käytetään nyt myös useissa muissakin ohjelmissa.

%description -l it
Libreria X scritta per GIMP. Viene usata da diversi programmi.

%description -l pl
Gtk+, która to biblioteka sta³a siê podstaw± programu Gimp, zawiera
funkcje do tworzenia graficznego interfejsu u¿ytkownika pod X Window.
By³a tworzona z za³o¿eniem ¿eby by³a ma³a, efektywna i wygodna. Gtk+
jest napisane w C z podej¶ciem zorientowanym bardzo obiektowo. Gdk
(czê¶æ Gtk+) jest warstw± po¶redni± pomiêdzy Xlib i reszt± toolkitu
zapewniaj±c± pracê niezale¿nie od g³êbi koloru (ilo¶ci bitów na
piksel). Gtk (druga czê¶æ Gtk+) jest natomiast ju¿ zbiorem ró¿nego
rodzaju kontrolek s³u¿±cych do tworzenia interfejsu u¿ytkownika.

%description -l pt_BR
Bibliotecas X originalmente escritas para o GIMP, que agora estão
sendo também usadas por vários outros programas.

%description -l tr
Baþlangýçta GIMP için yazýlmýþ X kitaplýklarý. Þu anda baþka
programlarca da kullanýlmaktadýr.

%package devel
Summary:	Gtk+ header files and development documentation
Summary(cs):	Sada nástrojù GIMP a kreslící kit GIMP
Summary(da):	GIMP Toolkit og GIMP Tegnings-værktøj
Summary(de):	GIMP Toolkit und GIMP Drawing Kit
Summary(es):	Conjunto de herramienta y conjunto de diseño GIMP
Summary(fi):	Gimp-työkalukokoelma ja Gimp-piirtotyökalut
Summary(fr):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK).
Summary(it):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl):	Pliki nag³ówkowe i dokumentacja do Gtk+ 
Summary(pt_BR):	Kit de ferramenta e kit de desenho GIMP
Summary(tr):	GIMP araç takýmý ve çizim takýmý
Group:		X11/Development/Libraries
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
Obsoletes:	libgtk+1.2-devel

%description devel
Libraries and header files for the GIMP's X libraries, which are
available as public libraries. GLIB includes generally useful data
structures, GDK is a drawing toolkit which provides a thin layer over
Xlib to help automate things like dealing with different color depths,
and GTK is a widget set for creating user interfaces.

%description -l es devel
Bibliotecas y archivos de inclusión del GIMP, que están disponibles
como bibliotecas públicas. GLIB incluye estructuras de datos útiles; e
GDK es un kit de herramientas que provee una camada sobre Xlib para
ayudar a automatizar cosas como el uso de diferentes profundidades de
color; y GTK es un conjunto de widgets para crear interfaces de
usuario.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do bibliotek Gtk+.

%description -l pt_BR devel
Bibliotecas e arquivos de inclusão do GIMP, que estão disponíveis como
bibliotecas públicas. A GLIB inclui estruturas de dados úteis; o GDK é
um kit de ferramentas que provê uma camada sobre a Xlib para ajudar a
automatizar coisas como o uso de diferentes profundidades de cor; e
GTK é um conjunto de widgets para criar interfaces de usuário.

%package static
Summary:	Gtk+ static libraries
Summary(es):	Bibliotecas estáticas del GIMP
Summary(pl):	Biblioteki statyczne Gtk+
Summary(pt_BR):	Bibliotecas estáticas do GIMP
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for the GIMP's X libraries, which are available as
public libraries.

%description -l es static
Bibliotecas estáticas del GIMP, que están disponibles como bibliotecas
públicas.

%description -l pl static
Biblioteki statyczne Gtk+.

%description -l pt_BR static
Bibliotecas estáticas do GIMP, que estão disponíveis como bibliotecas
públicas.

%prep
%setup  -q -a1 -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
#ibtoolize --copy --force
%{__gettextize}
#aclocal
#autoconf
#automake -a -c
cp -f /usr/share/automake/config.* .
%configure2_13 \
	--enable-debug=no \
	--enable-shm \
	--with-xinput=xfree

%{__make} m4datadir=%{_aclocaldir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

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

%dir %{_sysconfdir}/gtk
%lang(az) %{_sysconfdir}/gtk/gtkrc.az
%lang(be) %{_sysconfdir}/gtk/gtkrc.be
%lang(bg) %{_sysconfdir}/gtk/gtkrc.bg*
%lang(cs) %{_sysconfdir}/gtk/gtkrc.cs
%lang(cy) %{_sysconfdir}/gtk/gtkrc.cy
%lang(el) %{_sysconfdir}/gtk/gtkrc.el
%lang(eo) %{_sysconfdir}/gtk/gtkrc.eo
%lang(et) %{_sysconfdir}/gtk/gtkrc.et
%lang(ga) %{_sysconfdir}/gtk/gtkrc.ga
%lang(he) %{_sysconfdir}/gtk/gtkrc.he*
%lang(hr) %{_sysconfdir}/gtk/gtkrc.hr
%lang(hu) %{_sysconfdir}/gtk/gtkrc.hu
%lang(hy) %{_sysconfdir}/gtk/gtkrc.hy
%lang(ja) %{_sysconfdir}/gtk/gtkrc.ja
%lang(ka) %{_sysconfdir}/gtk/gtkrc.ka*
%lang(ko) %{_sysconfdir}/gtk/gtkrc.ko
%lang(lt) %{_sysconfdir}/gtk/gtkrc.lt
%lang(lv) %{_sysconfdir}/gtk/gtkrc.lv
%lang(mi) %{_sysconfdir}/gtk/gtkrc.mi
%lang(mk) %{_sysconfdir}/gtk/gtkrc.mk
%lang(pl) %{_sysconfdir}/gtk/gtkrc.pl
%lang(ro) %{_sysconfdir}/gtk/gtkrc.ro
%lang(ru) %{_sysconfdir}/gtk/gtkrc.ru*
%lang(sk) %{_sysconfdir}/gtk/gtkrc.sk
%lang(sp) %{_sysconfdir}/gtk/gtkrc.sp
%lang(sl) %{_sysconfdir}/gtk/gtkrc.sl
%lang(sq) %{_sysconfdir}/gtk/gtkrc.sq
%lang(sr) %{_sysconfdir}/gtk/gtkrc.sr
%lang(th) %{_sysconfdir}/gtk/gtkrc.th
%lang(tr) %{_sysconfdir}/gtk/gtkrc.tr
%lang(uk) %{_sysconfdir}/gtk/gtkrc.uk
%lang(vi) %{_sysconfdir}/gtk/gtkrc.vi*
%lang(yi) %{_sysconfdir}/gtk/gtkrc.yi
%lang(zh) %{_sysconfdir}/gtk/gtkrc.zh*
%lang(be,bg,mk,ru,sr,uk) %{_sysconfdir}/gtk/gtkrc.cp1251
%lang(he,yi) %{_sysconfdir}/gtk/gtkrc.cp1255
%lang(cs,hr,hu,pl,ro,sk,sl,sq,sr) %{_sysconfdir}/gtk/gtkrc.iso-8859-2
%lang(bg,mk,ru,sp,sr,uk) %{_sysconfdir}/gtk/gtkrc.iso-8859-5
%lang(et,lt,lv) %{_sysconfdir}/gtk/gtkrc.iso-8859-13
%lang(br,cy,ga) %{_sysconfdir}/gtk/gtkrc.iso-8859-14
%{_sysconfdir}/gtk/gtkrc.iso-8859-15

%dir %{_libdir}/gtk
%dir %{_libdir}/gtk/themes
%dir %{_libdir}/gtk/themes/engines
%dir %{_datadir}/themes

%{_datadir}/themes/Default

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO gtk/*.html gdk/*.html
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/*
%{_includedir}/*
%{_infodir}/*info*
%{_aclocaldir}/*.m4
%{_mandir}/man1/gtk-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
