Summary:     The Gimp Toolkit
Summary(pl): Gimp Toolkit
Name:        gtk+
Version:     1.1.9
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gimp.org/pub/gtk/v1.0/%{name}-%{version}.tar.gz
URL:         http://www.gtk.org/
Requires:    glib = %{version}
BuildRoot:   /tmp/%{name}-%{version}-root
Obsoletes:   gtk

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
Summary:     Gtk+ header files and development documentation
Summary(pl): Pliki nag³ówkowe i dokumentacja do Gtk+ 
Group:       X11/Libraries
Requires:    %{name} = %{version}, glib-devel = %{version}
Obsoletes:   gtk-devel
PreReq:      /sbin/install-info

%description devel
Header files and development documentation for the Gtk+ libraries.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek Gtk+.

%package static
Summary:     Gtk+ static libraries
Summary(pl): Biblioteki statyczne Gtk+
Group:       X11/Libraries
Requires:    %{name}-devel = %{version}

%description static
Gtk+ static libraries.

%description static -l pl
Biblioteki statyczne Gtk+

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure --prefix=/usr/X11R6 \
	--infodir=/usr/info \
	--enable-debug=no \
	--enable-shm
make m4datadir=/usr/share/aclocal

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=/usr/share/aclocal

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*so.*.*
gzip -9n $RPM_BUILD_ROOT/usr/{info/*info*,X11R6/man/man1/*}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/info/gdk.info.gz /usr/info-dir --entry \
"* GDK: (gdk).                                   The General Drawing Kit"
/sbin/install-info /usr/info/gtk.info.gz /usr/info-dir --entry \
"* GTK: (gtk).                                   The GIMP Toolkit"

%preun devel
/sbin/install-info --delete /usr/info/gdk.info.gz /usr/info-dir
/sbin/install-info --delete /usr/info/gtk.info.gz /usr/info-dir

%files
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*
/usr/X11R6/share/themes
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/gtk+.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/gtk+.mo

%files devel
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README TODO
/usr/X11R6/lib/lib*.so
/usr/X11R6/include/*
/usr/info/*info*gz
/usr/share/aclocal/*.m4
%attr(755, root, root) /usr/X11R6/bin/*
%attr(644, root,  man) /usr/X11R6/man/man1/gtk-config.1.gz

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*a

%changelog
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
