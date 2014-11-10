%define major 5
%define libname %mklibname KF5Activities %{major}
%define devname %mklibname KF5Activities -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kactivities
Version: 5.4.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%{version}/%{name}-%{version}.tar.xz
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
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: boost-devel
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
mv %{buildroot}%{_bindir}/kactivitymanagerd %{buildroot}%{_bindir}/kactivitymanagerd5
%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_bindir}/kactivitymanagerd5
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_libdir}/plugins/kactivitymanagerd
%{_libdir}/plugins/kactivitymanagerd_fileitem_linking_plugin.so
%{_libdir}/plugins/kcm_activities.so
%{_libdir}/plugins/kio_activities.so
%{_datadir}/kf5/kactivitymanagerd
%{_libdir}/qml/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_prefix}/mkspecs/*
%{_libdir}/pkgconfig/*
