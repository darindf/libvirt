Summary: Library providing an API to use the Xen virtualization
Name: libvirt
Version: 0.1.4
Release: 2
License: LGPL
Group: Development/Libraries
Source: libvirt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://libvir.org/
BuildRequires: python python-devel
Requires: xen
Requires: libxml2
Requires: readline
Requires: ncurses
BuildRequires: xen-devel >= 3.0.2-23
BuildRequires: libxml2-devel
BuildRequires: readline-devel
BuildRequires: ncurses-devel
Obsoletes: libvir
ExclusiveArch: i386 x86_64 ia64
Patch0: uuid_parse.patch

%description
This C library provides an API to use the Xen virtualization framework,
and the virsh command line tool to control virtual domains.

%package devel
Summary: Libraries, includes, etc. to compile with the libvirt library
Group: Development/Libraries
Requires: libvirt = %{version}
Obsoletes: libvir-devel

%description devel
Includes and documentations for the C library providing an API to use
the Xen virtualization framework

%package python
Summary: Python bindings for the libvirt library
Group: Development/Libraries
Requires: libvirt = %{version}
Obsoletes: libvir-python
Requires: %{_libdir}/python%(echo `python -c "import sys; print sys.version[0:3]"`)

%description python
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the Xen virtualization framework.

%prep
%setup -q
%patch0

%build
%configure
make

%install
rm -fr %{buildroot}

%makeinstall
(cd docs/examples ; make clean ; rm -rf .deps)
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.a

%clean
rm -fr %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING.LIB TODO
%doc %{_mandir}/man1/virsh.1*
%{_bindir}/virsh
%{_libdir}/lib*.so.*
%attr(4755, root, root) %{_libexecdir}/libvirt_proxy

%files devel
%defattr(-, root, root)

%{_libdir}/lib*.so
%{_includedir}/libvirt/*.h
%{_libdir}/pkgconfig/libvirt.pc
%doc %{_datadir}/gtk-doc/html/libvirt/*.devhelp
%doc %{_datadir}/gtk-doc/html/libvirt/*.html
%doc %{_datadir}/gtk-doc/html/libvirt/*.png
%doc %{_datadir}/gtk-doc/html/libvirt/*.css

%doc docs/*.html docs/html docs/*.gif
%doc docs/examples
%doc docs/libvirt-api.xml

%files python
%defattr(-, root, root)

%doc AUTHORS NEWS README COPYING.LIB
%{_libdir}/python*/site-packages/libvirt.py*
%{_libdir}/python*/site-packages/libvirtmod*
%doc python/tests/*.py
%doc python/TODO
%doc python/libvirtclass.txt
%doc docs/examples/python

%changelog
* Thu Aug 17 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-2
- patch to fix virParseUUID()

* Wed Aug 16 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-1
- vCPUs and affinity support
- more complete XML, console and boot options
- specific features support
- enforced read-only connections
- various improvements, bug fixes

* Wed Aug  2 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-6
- add patch from pvetere to allow getting uuid from libvirt

* Wed Aug  2 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-5
- build on ia64 now

* Thu Jul 27 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-4
- don't BR xen, we just need xen-devel

* Thu Jul 27 2006 Daniel Veillard <veillard@redhat.com> 0.1.3-3
- need rebuild since libxenstore is now versionned

* Mon Jul 24 2006 Mark McLoughlin <markmc@redhat.com> - 0.1.3-2
- Add BuildRequires: xen-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.1.3-1.1
- rebuild

* Tue Jul 11 2006 Daniel Veillard <veillard@redhat.com> 0.1.3-1
- support for HVM Xen guests
- various bugfixes

* Mon Jul  3 2006 Daniel Veillard <veillard@redhat.com> 0.1.2-1
- added a proxy mechanism for read only access using httpu
- fixed header includes paths

* Wed Jun 21 2006 Daniel Veillard <veillard@redhat.com> 0.1.1-1
- extend and cleanup the driver infrastructure and code
- python examples
- extend uuid support
- bug fixes, buffer handling cleanups
- support for new Xen hypervisor API
- test driver for unit testing
- virsh --conect argument

* Mon Apr 10 2006 Daniel Veillard <veillard@redhat.com> 0.1.0-1
- various fixes
- new APIs: for Node information and Reboot
- virsh improvements and extensions
- documentation updates and man page
- enhancement and fixes of the XML description format

* Tue Feb 28 2006 Daniel Veillard <veillard@redhat.com> 0.0.6-1
- added error handling APIs
- small bug fixes
- improve python bindings
- augment documentation and regression tests

* Thu Feb 23 2006 Daniel Veillard <veillard@redhat.com> 0.0.5-1
- new domain creation API
- new UUID based APIs
- more tests, documentation, devhelp
- bug fixes

* Fri Feb 10 2006 Daniel Veillard <veillard@redhat.com> 0.0.4-1
- fixes some problems in 0.0.3 due to the change of names

* Wed Feb  8 2006 Daniel Veillard <veillard@redhat.com> 0.0.3-1
- changed library name to libvirt from libvir, complete and test the python 
  bindings

* Sun Jan 29 2006 Daniel Veillard <veillard@redhat.com> 0.0.2-1
- upstream release of 0.0.2, use xend, save and restore added, python bindings
  fixed

* Wed Nov  2 2005 Daniel Veillard <veillard@redhat.com> 0.0.1-1
- created
