%define major		0
%define libname		lib%{name}
%define fulllibname	%mklibname %{name} %{major}
%define develname	%mklibname -d %{name}

Name:		a52dec
Version:	0.7.4
Release:	18
Summary:	A free ATSC A/52 stream decoder library
License:	GPLv2+
Group:		Video
URL:		http://liba52.sourceforge.net
Source:		%{name}-%{version}.tar.bz2
Patch0:		a52dec-0.7.4-pic.patch
BuildRequires:	autoconf2.5
BuildRequires:	chrpath
Provides:	liba52-apps
Requires:	%{fulllibname} = %{version}-%{release}


%description
liba52 is a free library for decoding ATSC A/52 streams.

The A/52 standard is used in a variety of applications, including
digital television and DVD. It is also known as AC-3.

%package -n %{fulllibname}
Summary:	Libraries for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	liba52dec_0 = %{version}-%{release}
Provides:	liba52_0 = %{version}-%{release}
Provides:	liba520 = %{version}-%{release}

%description -n %{fulllibname}
liba52 is a free library for decoding ATSC A/52 streams.

The A/52 standard is used in a variety of applications, including
digital television and DVD. It is also known as AC-3.

This package contains libraries needed to run programs linked with %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{fulllibname} = %{version}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
liba52 is a free library for decoding ATSC A/52 streams.

The A/52 standard is used in a variety of applications, including
digital television and DVD. It is also known as AC-3.

This package contains development files needed to compile programs which
use %{name}.

%prep
%setup -q
%patch0 -p1 -b .pic
autoconf

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x --enable-shared --disable-static
%make

%install
%makeinstall_std
chrpath -d %{buildroot}%{_bindir}/a52dec

%files
%doc AUTHORS COPYING NEWS README TODO HISTORY
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{fulllibname}
%{_libdir}/liba52.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.4-16mdv2011.0
+ Revision: 662747
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.4-15mdv2011.0
+ Revision: 603165
- rebuild

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 0.7.4-14mdv2010.1
+ Revision: 506946
- rebuild for missing SRPM

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.4-13mdv2010.0
+ Revision: 413017
- rebuild

* Tue Jan 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.4-12mdv2009.1
+ Revision: 331898
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.7.4-11mdv2009.0
+ Revision: 220324
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jan 03 2008 Thierry Vignaud <tv@mandriva.org> 0.7.4-10mdv2008.1
+ Revision: 141937
- compile with -fPIC
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.4-9mdv2008.1
+ Revision: 101720
- new devel name
- update license tag
- unpack patch

* Wed May 23 2007 Christiaan Welvaart <spturtle@mandriva.org> 0.7.4-9mdv2008.0
+ Revision: 30217
- Import a52dec



* Thu Aug 24 2006 Götz Waschk <waschk@mandriva.org> 0.7.4-9mdv2007.0
- small fixes

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.7.4-8mdk
- Rebuild

* Fri Jun 10 2005 Götz Waschk <waschk@mandriva.org> 0.7.4-7mdk
- Rebuild

* Tue Jun  8 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-6mdk
- fix descriptions (Thierry Vignaud)

* Fri Oct 24 2003 Stefan van der Eijk <stefan@eijk.nu> 0.7.4-5mdk
- BuildRequires

* Thu Oct  2 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.7.4-4mdk
- workaround build on amd64

* Thu Jul 10 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-3mdk
- autoconf2.5 macro

* Sat Jan 04 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.7.4-2mdk
- rebuild

* Wed Sep 25 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.7.4-1mdk
- 0.7.4

* Mon May 06 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.7.3-5mdk
- Add missing requires to lib

* Wed Apr 17 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.7.3-4mdk
- libname is liba52dec0
- obsoletes tags to make upgrade easier

* Tue Apr 16 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.7.3-3mdk
- reverted name to a52dec and libname to liba52dec

* Mon Apr 15 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.7.3-2mdk
- libname is liba52_0

* Mon Apr 15 2002 Guillaume Rousse <rousse@ccr.jussieu.fr> 0.7.3-1mdk
- first mdk release

* Fri Mar 29 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.7.3-1plf 
	Create package from Michael Reinsch <mr@uue.org>
		- first plf package
