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
Release:	17
Epoch:		1
License:	LGPL
Group:		X11/Libraries
# Source0-md5:	4d5cb2fc7fb7830e4af9747a36bfce20
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.2/%{name}-%{version}.tar.gz
# Source1-md5:	b80957f7e3148dc3b540fba0c88e51e5
Source1:	http://developer.gnome.org/doc/API/gdk-docs.tar.gz
# Source2-md5:	ae1d6638d1c4799a4a328f27f62aa224
Source2:	http://developer.gnome.org/doc/API/gtk-docs.tar.gz
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
URL:		http://www.gtk.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= %{version}
BuildRequires:	libtool >= 1.4.2-9
BuildRequires:	texinfo
Requires:	glib >= %{version}
Requires:	iconv
Obsoletes:	libgtk+1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK+ is written in C with a very
object-oriented approach. GDK (part of GTK+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and GTK is a widget set for
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
GTK+, która to biblioteka sta³a siê podstaw± programu Gimp, zawiera
funkcje do tworzenia graficznego interfejsu u¿ytkownika pod X Window.
By³a tworzona z za³o¿eniem ¿eby by³a ma³a, efektywna i wygodna. GTK+
jest napisane w C z podej¶ciem zorientowanym bardzo obiektowo. GDK
(czê¶æ GTK+) jest warstw± po¶redni± pomiêdzy Xlib i reszt± toolkitu
zapewniaj±c± pracê niezale¿nie od g³êbi koloru (ilo¶ci bitów na
piksel). GTK (druga czê¶æ GTK+) jest natomiast ju¿ zbiorem ró¿nego
rodzaju kontrolek s³u¿±cych do tworzenia interfejsu u¿ytkownika.

%description -l pt_BR
Bibliotecas X originalmente escritas para o GIMP, que agora estão
sendo também usadas por vários outros programas.

%description -l tr
Baþlangýçta GIMP için yazýlmýþ X kitaplýklarý. Þu anda baþka
programlarca da kullanýlmaktadýr.

%package devel
Summary:	GTK+ header files and development documentation
Summary(cs):	Sada nástrojù GIMP a kreslící kit GIMP
Summary(da):	GIMP Toolkit og GIMP Tegnings-værktøj
Summary(de):	GIMP Toolkit und GIMP Drawing Kit
Summary(es):	Conjunto de herramienta y conjunto de diseño GIMP
Summary(fi):	Gimp-työkalukokoelma ja Gimp-piirtotyökalut
Summary(fr):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK)
Summary(it):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl):	Pliki nag³ówkowe i dokumentacja do GTK+
Summary(pt_BR):	Kit de ferramenta e kit de desenho GIMP
Summary(tr):	GIMP araç takýmý ve çizim takýmý
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib-devel >= %{version}
# Every program using GTK+ should get a list of libraries to link with by
# executing `gtk-config --libs`. All libraries listed below are returned by
# this call, so they are required by every program compiled with GTK+.
Requires:	XFree86-devel
Requires:	glib-devel
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

%description devel -l es
Bibliotecas y archivos de inclusión del GIMP, que están disponibles
como bibliotecas públicas. GLIB incluye estructuras de datos útiles; e
GDK es un kit de herramientas que provee una camada sobre Xlib para
ayudar a automatizar cosas como el uso de diferentes profundidades de
color; y GTK es un conjunto de widgets para crear interfaces de
usuario.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek GTK+.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão do GIMP, que estão disponíveis como
bibliotecas públicas. A GLIB inclui estruturas de dados úteis; o GDK é
um kit de ferramentas que provê uma camada sobre a Xlib para ajudar a
automatizar coisas como o uso de diferentes profundidades de cor; e
GTK é um conjunto de widgets para criar interfaces de usuário.

%package static
Summary:	GTK+ static libraries
Summary(es):	Bibliotecas estáticas del GIMP
Summary(pl):	Biblioteki statyczne GTK+
Summary(pt_BR):	Bibliotecas estáticas do GIMP
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libraries for the GIMP's X libraries, which are available as
public libraries.

%description static -l es
Bibliotecas estáticas del GIMP, que están disponibles como bibliotecas
públicas.

%description static -l pl
Biblioteki statyczne GTK+.

%description static -l pt_BR
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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

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
