# TODO
# - some nice patches: http://www.acm.uiuc.edu/sigunix/projects/bugfixes/
Summary:	The Gimp Toolkit
Summary(cs.UTF-8):	Sada nástrojů pro Gimp
Summary(de.UTF-8):	Der Gimp-Toolkit
Summary(es.UTF-8):	Conjunto de herramientas Gimp
Summary(fi.UTF-8):	Gimp-työkalukokoelma
Summary(fr.UTF-8):	Le toolkit de Gimp
Summary(it.UTF-8):	Il toolkit per Gimp
Summary(pl.UTF-8):	Gimp Toolkit
Summary(pt_BR.UTF-8):	Kit de ferramentas Gimp
Summary(tr.UTF-8):	Gimp ToolKit arayüz kitaplığı
Name:		gtk+
Version:	1.2.10
Release:	23
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.2/%{name}-%{version}.tar.gz
# Source0-md5:	4d5cb2fc7fb7830e4af9747a36bfce20
Source1:	http://developer.gnome.org/doc/API/gdk-docs.tar.gz
# Source1-md5:	b80957f7e3148dc3b540fba0c88e51e5
Source2:	http://developer.gnome.org/doc/API/gtk-docs.tar.gz
# Source2-md5:	ae1d6638d1c4799a4a328f27f62aa224
Patch0:		%{name}-info.patch
Patch1:		%{name}-ahiguti.patch
Patch2:		%{name}-strip.patch
Patch3:		%{name}-pkgconfig.patch
Patch4:		%{name}-focus.patch
Patch5:		%{name}-am_fix.patch
Patch6:		%{name}-ac_fix.patch
Patch7:		%{name}-localenames.patch
Patch8:		%{name}-link.patch
Patch9:		%{name}-am18.patch
Patch10:	format-security.patch
URL:		http://www.gtk.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-tools
BuildRequires:	glib-devel >= %{version}
BuildRequires:	libtool >= 1.4.2-9
BuildRequires:	texinfo
# libXext already implied by libXi
BuildRequires:	xorg-lib-libXi-devel
Requires:	glib >= %{version}
Requires:	iconv
Obsoletes:	libgtk+1.2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK+ is written in C with a very
object-oriented approach. GDK (part of GTK+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and GTK is a widget set for
creating user interfaces.

%description -l cs.UTF-8
Knihovny X původně psané pro GIMP, které nyní používá také řada jiných
programů.

%description -l da.UTF-8
X biblioteker, oprindeligt udviklet til GIMP, men anvendes nu af flere
forskellige programmer.

%description -l de.UTF-8
Die X-Libraries, die ursprünglich für GIMP geschrieben wurden und
mittlerweile für eine ganze Reihe anderer Programme benutzt werden.

%description -l fr.UTF-8
X-kirjastot, jotka alunperin kirjoitettiin GIMP:lle, mutta joita
käytetään nyt myös useissa muissakin ohjelmissa.

%description -l it.UTF-8
Libreria X scritta per GIMP. Viene usata da diversi programmi.

%description -l pl.UTF-8
GTK+, która to biblioteka stała się podstawą programu Gimp, zawiera
funkcje do tworzenia graficznego interfejsu użytkownika pod X Window.
Była tworzona z założeniem żeby była mała, efektywna i wygodna. GTK+
jest napisane w C z podejściem zorientowanym bardzo obiektowo. GDK
(część GTK+) jest warstwą pośrednią pomiędzy Xlib i resztą toolkitu
zapewniającą pracę niezależnie od głębi koloru (ilości bitów na
piksel). GTK (druga część GTK+) jest natomiast już zbiorem różnego
rodzaju kontrolek służących do tworzenia interfejsu użytkownika.

%description -l pt_BR.UTF-8
Bibliotecas X originalmente escritas para o GIMP, que agora estão
sendo também usadas por vários outros programas.

%description -l tr.UTF-8
Başlangıçta GIMP için yazılmış X kitaplıkları. Şu anda başka
programlarca da kullanılmaktadır.

%package devel
Summary:	GTK+ header files and development documentation
Summary(cs.UTF-8):	Sada nástrojů GIMP a kreslící kit GIMP
Summary(da.UTF-8):	GIMP Toolkit og GIMP Tegnings-værktøj
Summary(de.UTF-8):	GIMP Toolkit und GIMP Drawing Kit
Summary(es.UTF-8):	Conjunto de herramienta y conjunto de diseño GIMP
Summary(fi.UTF-8):	Gimp-työkalukokoelma ja Gimp-piirtotyökalut
Summary(fr.UTF-8):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK)
Summary(it.UTF-8):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do GTK+
Summary(pt_BR.UTF-8):	Kit de ferramenta e kit de desenho GIMP
Summary(tr.UTF-8):	GIMP araç takımı ve çizim takımı
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib-devel >= %{version}
# Every program using GTK+ should get a list of libraries to link with by
# executing `gtk-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with GTK+.
Requires:	glib-devel >= %{version}
Requires:	xorg-lib-libXi-devel
Obsoletes:	libgtk+1.2-devel
Conflicts:	autoconf < 2.13
Conflicts:	automake < 1.4
Conflicts:	libtool < 1.3.2

%description devel
Libraries and header files for the GIMP's X libraries, which are
available as public libraries. GLIB includes generally useful data
structures, GDK is a drawing toolkit which provides a thin layer over
Xlib to help automate things like dealing with different color depths,
and GTK is a widget set for creating user interfaces.

%description devel -l es.UTF-8
Bibliotecas y archivos de inclusión del GIMP, que están disponibles
como bibliotecas públicas. GLIB incluye estructuras de datos útiles; e
GDK es un kit de herramientas que provee una camada sobre Xlib para
ayudar a automatizar cosas como el uso de diferentes profundidades de
color; y GTK es un conjunto de widgets para crear interfaces de
usuario.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek GTK+.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão do GIMP, que estão disponíveis como
bibliotecas públicas. A GLIB inclui estruturas de dados úteis; o GDK é
um kit de ferramentas que provê uma camada sobre a Xlib para ajudar a
automatizar coisas como o uso de diferentes profundidades de cor; e
GTK é um conjunto de widgets para criar interfaces de usuário.

%package static
Summary:	GTK+ static libraries
Summary(es.UTF-8):	Bibliotecas estáticas del GIMP
Summary(pl.UTF-8):	Biblioteki statyczne GTK+
Summary(pt_BR.UTF-8):	Bibliotecas estáticas do GIMP
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libraries for the GIMP's X libraries, which are available as
public libraries.

%description static -l es.UTF-8
Bibliotecas estáticas del GIMP, que están disponibles como bibliotecas
públicas.

%description static -l pl.UTF-8
Biblioteki statyczne GTK+.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas do GIMP, que estão disponíveis como bibliotecas
públicas.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

mv -f po/{no,nb}.po
mv -f po/{sr,sr@Latn}.po
mv -f po/{sp,sr}.po
mv -f po/{zh_CN.GB2312,zh_CN}.po
mv -f po/{zh_TW.Big5,zh_TW}.po
rm -f po/{no,sp,sr,zh*}.gmo

mkdir gtk-doc
tar xzf %{SOURCE1} -C gtk-doc
tar xzf %{SOURCE2} -C gtk-doc

%build
rm -f missing aclocal.m4 acinclude.m4
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-debug=no \
	--enable-shm \
	--with-x \
	--with-xinput=xfree

%{__make} \
	m4datadir=%{_aclocaldir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gtk/themes/engines

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

[ -d $RPM_BUILD_ROOT%{_localedir}/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_localedir}/sr@{Latn,latin}
%find_lang %{name}

%{__rm} -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libgdk-1.2.so.*.*
%ghost %{_libdir}/libgdk-1.2.so.0
%attr(755,root,root) %{_libdir}/libgtk-1.2.so.*.*
%ghost %{_libdir}/libgtk-1.2.so.0

%dir %{_sysconfdir}/gtk
%lang(az) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.az
%lang(be) %{_sysconfdir}/gtk/gtkrc.be
%lang(bg) %{_sysconfdir}/gtk/gtkrc.bg*
%lang(cs) %{_sysconfdir}/gtk/gtkrc.cs
%lang(cy) %{_sysconfdir}/gtk/gtkrc.cy
%lang(el) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.el
%lang(eo) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.eo
%lang(et) %{_sysconfdir}/gtk/gtkrc.et
%lang(ga) %{_sysconfdir}/gtk/gtkrc.ga
%lang(he) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.he
%lang(he) %{_sysconfdir}/gtk/gtkrc.he_*
%lang(hr) %{_sysconfdir}/gtk/gtkrc.hr
%lang(hu) %{_sysconfdir}/gtk/gtkrc.hu
%lang(hy) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.hy
%lang(ja) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.ja
%lang(ka) %{_sysconfdir}/gtk/gtkrc.ka*
%lang(ko) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.ko
%lang(lt) %{_sysconfdir}/gtk/gtkrc.lt
%lang(lv) %{_sysconfdir}/gtk/gtkrc.lv
%lang(mi) %{_sysconfdir}/gtk/gtkrc.mi
%lang(mk) %{_sysconfdir}/gtk/gtkrc.mk
%lang(pl) %{_sysconfdir}/gtk/gtkrc.pl
%lang(ro) %{_sysconfdir}/gtk/gtkrc.ro
%lang(ru) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.ru
%lang(ru) %{_sysconfdir}/gtk/gtkrc.ru_RU.iso88595
%lang(sk) %{_sysconfdir}/gtk/gtkrc.sk
%lang(sl) %{_sysconfdir}/gtk/gtkrc.sl
# "sp" was meant to be "sr@cyrillic"
%lang(sr) %{_sysconfdir}/gtk/gtkrc.sp
%lang(sq) %{_sysconfdir}/gtk/gtkrc.sq
%lang(sr) %{_sysconfdir}/gtk/gtkrc.sr
%lang(th) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.th
%lang(tr) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.tr
%lang(uk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.uk
%lang(vi) %{_sysconfdir}/gtk/gtkrc.vi
%lang(vi) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.vi_VN.tcvn
%lang(vi) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.vi_VN.viscii
%lang(vi) %{_sysconfdir}/gtk/gtkrc.vi_VN.viscii111
%lang(yi) %{_sysconfdir}/gtk/gtkrc.yi
%lang(zh) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.zh_CN
%lang(zh) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.zh_TW.big5
%lang(be,bg,mk,ru,sr,uk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.cp1251
%lang(he,yi) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.cp1255
%lang(cs,hr,hu,pl,ro,sk,sl,sq,sr) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.iso-8859-2
%lang(bg,mk,ru,sr,uk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.iso-8859-5
%lang(et,lt,lv) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.iso-8859-13
%lang(br,cy,ga) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.iso-8859-14
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk/gtkrc.iso-8859-15

%dir %{_libdir}/gtk
%dir %{_libdir}/gtk/themes
%dir %{_libdir}/gtk/themes/engines

%{_datadir}/themes/Default/gtk

%files devel
%defattr(644,root,root,755)
%doc ChangeLog gtk-doc/{gdk,gtk}
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/*
%{_includedir}/*
%{_infodir}/*.info*
%{_aclocaldir}/*.m4
%{_mandir}/man1/gtk-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
