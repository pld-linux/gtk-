Summary:	The Gimp Toolkit
Summary(pl):	Gimp Toolkit
Name:		gtk+
Version:	1.2.2
Release:	2
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gimp.org/pub/gtk/v1.1/%{name}-%{version}.tar.gz
Patch0:		gtk+-info.patch
URL:		http://www.gtk.org/
Icon:		gtk+.gif
Requires:	glib = %{version}
BuildPrereq:	glib-devel = %{version}
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gtk

%description
Gtk+, which stands for the Gimp ToolKit, is a library for creating graphical
user interfaces for the X Window System. It is designed to be small,
efficient, and flexible. Gtk+ is written in C with a very object-oriented
approach.
Gdk (part of Gtk+) is a drawing toolkit which provides a thin layer over
Xlib to help automate things like dealing with different color depths, and
Gtk is a widget set for creating user interfaces.

%description -l pl
Gtk+, któtra to biblioteka sta³a siê podstaw± programu Gimp zawiera funkcje
do tworzenia graficznego interfrjsu uzytkownika pod X Window. By³a tworzona
z za³o¿eniem ¿eby bya ma³a, efektywna i wygodna. Gtk+ jest napiane w C z
podej¶ciem zorientowanym bardzo obiektowo.
Gdk (czê¶æ Gtk+) jest warsw± po¶redni± pomiêdzy Xlib i reszt± toolkit
zapewniaj±c± pracê niezale¿nie od g³êbi koloru (ilo¶ci bitów na piksel).
Gtk (druga czê¶æ Gtk+) jest natomiast ju¿ zbiorem ró¿nego rodzaju kontrolek
s³u¿±cych do tworzenia interfejsu u¿ytkownika.

%package devel
Summary:	Gtk+ header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do Gtk+ 
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
PreReq:		/sbin/install-info
Requires:	%{name} = %{version}
Requires:	glib-devel = %{version}
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	libtool  >= 1.2d
Obsoletes:	gtk-devel

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
%setup -q
%patch0 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6 \
	--infodir=/usr/info \
	--sysconfdir=/etc/X11 \
	--enable-debug=no \
	--enable-shm

make m4datadir=/usr/share/aclocal

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=/usr/share/aclocal \
	gnulocaledir=$RPM_BUILD_ROOT/usr/X11R6/share/locale

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*so.*.*

gzip -9n $RPM_BUILD_ROOT/usr/{info/*info*,X11R6/share/man/man1/*} \
	AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/share/info/gdk.info.gz /etc/info-dir
/sbin/install-info /usr/share/info/gtk.info.gz /etc/info-dir

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/share/info/gdk.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/share/info/gtk.info.gz /etc/info-dir
fi

%files
%defattr(644,root,root,755) 
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

%lang(ja) /etc/X11/gtk/gtkrc.ja
%lang(ko) /etc/X11/gtk/gtkrc.ko
%lang(ru) /etc/X11/gtk/gtkrc.ru

%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/gtk+.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/gtk+.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/gtk+.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/gtk+.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/gtk+.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/gtk+.mo
%lang(ja) /usr/X11R6/share/locale/ja/LC_MESSAGES/gtk+.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/gtk+.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/gtk+.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/gtk+.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/gtk+.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/gtk+.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/gtk+.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/gtk+.mo

/usr/X11R6/share/themes

%files devel
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) /usr/X11R6/lib/lib*.so
%attr(755,root,root) /usr/X11R6/bin/*

/usr/X11R6/include/*
/usr/share/info/*info*gz
/usr/share/aclocal/*.m4

/usr/X11R6/share/man/man1/gtk-config.1.gz

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/lib*.a

%changelog
* Mon May 10 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.2-2]
- now package is FHS 2.0 compiliat,
- added package icon.

* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.2-1]
- removed Conflicts: glibc <= 2.0.7 (not neccessary now),
- added "BuildPrereq: glib = %%{version}".

* Thu Mar 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.1-1]
- gzipping %doc,
- added --sysconfdir=/etc/X11/gtk to ./configure parameters.

* Sat Feb 27 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.0-1]
- changed Grouop to X11/Development/Libraries in devel, static,
- added "Conflicts: glibc <= 2.0.7" for prevent install
  with proper version glibc.

* Wed Feb 24 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.16-1]
- more locales (ru),
- removed man group from man pages.

* Tue Jan 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.13-1d]
- more locales (cs, es, it),
- adde Group(pl),
- added "Requires: autoconf >= 2.13, automake >= 1.4, libtool >= 1.2d"
  for devel subpackage.

* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.12-1]
- more locales (ko).

* Sat Jan 01 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.11-1]
- standarized {un}registering info pages (added gtk+-info.patch),
- added Group(pl),
- more locales (fr, ja, nl, no, pl, sv).

* Sat Dec 19 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.7-2]
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment,
- changed dependencies to "Requires: glib = %%{version}" in main and
  "Requires: glib-devel = %%{version}" in devel subpackage,
- added --enable-debug=no and --enable-shm for ./configure parameters,
- standarized {un}registering info pages.

* Tue Nov 24 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.5-1]
- rewrited Summary and %description,
- added pl translation,
- updated "Requires: glib >= 1.1.5",
- fixed --entry text on {un}registering info page for ed in %post
  %preun in devel.

* Thu Sep 24  1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.2-1]
- added man page for gtk-config in devel,
- added "Requires: glib >= 1.1.3" for main package.

* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.1-2]
- changed prefix to /usr/X11R6.

* Thu Aug  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.1-1]
- removed glib stuff (nowe in separated package),
- removed glib from Obsoletes:,
- changed permission on shared libs to 755,
- devel %postun changed to %preun,
- fiew simplification in %files,
- rewrited some %descriprion and Summary,
- added static subpackage.

* Sat Jun  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.4-1]
- added -q %setup parameter,
- added using %%{name} macro in Buildroot,
- removed glib subpackage,
- removed /usr/{info/dir.gz,lib/lib*la} files and /usr/lib/lib*so.* links
  from devel,
- removed COPING from %doc (copyright statment is in Copyright field),
- simplification in %build and %install,
- added installing glib info page in info indeks,
- changesed dependences for devel to "Requires: %%{name} = %%{version}"
- added stripping shared libs.

* Mon May 04 1998 Michael Fulbright <msf@redhat.com>
- updated to latest CVS gtk-1-0 - version 1.0.1

* Fri May 01 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated to latest CVS gtk-1-0 for imlib fix

* Mon Apr 13 1998 Marc Ewing <marc@redhat.com>
- Split out glib package

* Tue Apr  8 1998 Shawn T. Amundson <amundson@gtk.org>
- Changed version to 1.0.0

* Tue Apr  7 1998 Owen Taylor <otaylor@gtk.org>
- Changed version to 0.99.10

* Thu Mar 19 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.9
- Changed gtk home page to www.gtk.org

* Thu Mar 19 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.8

* Sun Mar 15 1998 Marc Ewing <marc@redhat.com>
- Added aclocal and bin stuff to file list.
- Added -k to the SMP make line.
- Added lib/glib to file list.

* Fri Mar 14 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.7

* Fri Mar 14 1998 Shawn T. Amundson <amundson@gimp.org>
- Updated ftp url and changed version to 0.99.6

* Thu Mar 12 1998 Marc Ewing <marc@redhat.com>
- Reworked to integrate into gtk+ source tree

- Truncated ChangeLog.  Previous Authors:
  Trond Eivind Glomsrod <teg@pvv.ntnu.no>
  Michael K. Johnson <johnsonm@redhat.com>
  Otto Hammersmith <otto@redhat.com>
