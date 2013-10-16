%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}

Summary:	A free ATSC A/52 stream decoder library
Name:		a52dec
Version:	0.7.4
Release:	20
License:	GPLv2+
Group:		Video
Url:		http://liba52.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
Patch0:		a52dec-0.7.4-pic.patch

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
%setup -q
%apply_patches
autoconf

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
	--enable-shared \
	--disable-static
%make

%install
%makeinstall_std
chrpath -d %{buildroot}%{_bindir}/a52dec

%files
%doc AUTHORS COPYING NEWS README TODO HISTORY
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/liba52.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so

