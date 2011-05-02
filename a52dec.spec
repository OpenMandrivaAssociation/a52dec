%define name		a52dec
%define major		0
%define libname		lib%{name}
%define fulllibname	%mklibname %{name} %{major}
%define develname %mklibname -d %name
%define version 0.7.4
%define release %mkrel 16

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A free ATSC A/52 stream decoder library
License:	GPLv2+
Group:		Video
URL:		http://liba52.sourceforge.net
Source:		%{name}-%{version}.tar.bz2
Patch0:		a52dec-0.7.4-pic.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Obsoletes:	liba52-apps
Provides:	liba52-apps
Requires:	%{fulllibname} = %{version}
BuildRequires:	autoconf2.5
BuildRequires:	chrpath

%description
liba52 is a free library for decoding ATSC A/52 streams.

The A/52 standard is used in a variety of applications, including
digital television and DVD. It is also known as AC-3.

%package -n %{fulllibname}
Summary:	Libraries for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	liba52dec_0
Obsoletes:	liba52_0
Obsoletes:	liba520
Provides:	liba52dec_0
Provides:	liba52_0
Provides:	liba520

%description -n %{fulllibname}
liba52 is a free library for decoding ATSC A/52 streams.

The A/52 standard is used in a variety of applications, including
digital television and DVD. It is also known as AC-3.

This package contains libraries needed to run programs linked with %{name}.

%package -n %develname
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{fulllibname} = %{version}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	liba52dec_0-devel
Obsoletes:	liba52_0-devel
Obsoletes:	liba520-devel
Obsoletes: %mklibname -d %name 0

%description -n %develname
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
export CFLAGS="%optflags -fPIC"
%configure2_5x --enable-shared
%make

%install
rm -rf %buildroot
%makeinstall
chrpath -d %buildroot%_bindir/a52dec

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{fulllibname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{fulllibname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO HISTORY
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{fulllibname}
%defattr(-,root,root)
%{_libdir}/liba52.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
