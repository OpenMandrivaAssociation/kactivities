%define major 5
%define libname %mklibname KF5Activities %{major}
%define devname %mklibname KF5Activities -d
%define debug_package %{nil}

Name: kactivities
Version: 4.99.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 Activities framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
KDE Frameworks 5 Activities framework

%package -n %{libname}
Summary: KDE Frameworks 5 Activities framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 Activities framework

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Activities library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Activities library

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_bindir}/kactivitymanagerd
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_libdir}/plugins/kactivitymanagerd
%{_libdir}/qml

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_prefix}/mkspecs/*
%{_libdir}/pkgconfig/*
