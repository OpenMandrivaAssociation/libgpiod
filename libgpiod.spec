%define major 2
%define lib %mklibname gpiod %{major}
%define dev %mklibname -d gpiod

Name:		libgpiod
Version:	1.6.3
Release:	1
License:	LGPLv3+
Source0:	https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-%{version}.tar.gz
Group:		System
Summary:	Library for talking to GPIO interfaces

%description
Library for talking to GPIO interfaces

%package -n %{lib}
Summary:	Library for talking to GPIO interfaces

%description -n %{lib}
Library for talking to GPIO interfaces

%package -n %{dev}
Summary:	Development files for the libgpiod GPIO library
Requires:	%{lib} = %{EVRD}

%description -n %{dev}
Development files for the libgpiod GPIO library

%prep
%autosetup -p1
[ -e autogen.sh ] && ./autogen.sh
%configure

%build
%make_build

%install
%make_install

%files -n %{lib}
%{_libdir}/libgpiod.so.%{major}*

%files -n %{dev}
%{_libdir}/libgpiod.so
%{_libdir}/pkgconfig/libgpiod.pc
%{_includedir}/gpiod.h
