%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}
%define _disable_lto 1

Summary:	A free ATSC A/52 stream decoder library
Name:		a52dec
Version:	0.8.0
Release:	1
License:	GPLv2+
Group:		Video
Url:		https://git.adelielinux.org/community/a52dec
Source0:	https://git.adelielinux.org/community/a52dec/-/archive/v%{version}/a52dec-v%{version}.tar.bz2

BuildRequires:	chrpath
Provides:	liba52-apps

%description
liba52 is a free library for decoding ATSC A/52 streams.

The A/52 standard is used in a variety of applications, including
digital television and DVD. It is also known as AC-3.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains libraries needed to run programs linked with %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development files needed to compile programs which
use %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}
./bootstrap
export CFLAGS="%{optflags} -fPIC"
%configure \
	--enable-shared

%build
%make_build

%install
%make_install
chrpath -d %{buildroot}%{_bindir}/a52dec

%files
%doc AUTHORS COPYING NEWS README TODO HISTORY
%{_bindir}/*
%doc %{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/liba52.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
