Summary:   The Gimp Toolkit
Name:      gtk+
Version:   1.1.1
Release:   1
Copyright: LGPL
Group:     X11/Libraries
Source:    ftp://ftp.gimp.org/pub/gtk/v1.0/%{name}-%{version}.tar.gz
URL:       http://www.gtk.org/
BuildRoot: /tmp/%{name}-%{version}-root
Obsoletes: gtk

%description
The X libraries originally written for the GIMP, which are now used by
several other programs as well.

%package devel
Summary:   Gtk+ header files and development documentation
Group:     X11/Libraries
Requires:  %{name} = %{version}
Obsoletes: gtk-devel
PreReq:    /sbin/install-info

%description devel
Header files and development documentation for the GIMP's X libraries, which
are available as public libraries. GDK is a drawing toolkit which provides a
thin layer over Xlib to help automate things like dealing with different
color depths, and GTK is a widget set for creating user interfaces.

%package static
Summary:   Gtk+ static librariess
Group:     X11/Libraries
Requires:  %{name}-devel = %{version}

%description static
Static libraries ot the GIMP's X libraries, which are available as public
libraries. GDK is a drawing toolkit which provides a thin layer over Xlib to
help automate things like dealing with different color depths, and GTK is a
widget set for creating user interfaces.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

gzip -9n $RPM_BUILD_ROOT/usr/info/*info*

strip $RPM_BUILD_ROOT/usr/lib/lib*so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/info/gdk.info.gz /usr/info/dir
/sbin/install-info /usr/info/gtk.info.gz /usr/info/dir

%preun devel
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/gdk.info.gz /usr/info/dir
    /sbin/install-info --delete /usr/info/gtk.info.gz /usr/info/dir
fi

%files
%attr(755, root, root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README TODO
/usr/lib/lib*.so
/usr/include/*
/usr/info/*info*gz
/usr/share/aclocal/*.m4
%attr(755, root, root) /usr/bin/*

%files static
%attr(644, root, root) /usr/lib/lib*a

%changelog
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
- added striping shared libs.

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
