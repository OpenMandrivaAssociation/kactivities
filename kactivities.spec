%define major 5
%define libname %mklibname KF5Activities %{major}
%define devname %mklibname KF5Activities -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kactivities
Version: 5.18.0
Release: 2
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 Activities framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
Patch0: kactivities-5.18.0-soname.patch
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: boost-devel
Requires: %{libname} = %{EVRD}

%description
KDE Frameworks 5 Activities framework.

%package -n %{libname}
Summary: KDE Frameworks 5 Activities framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 Activities framework.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Activities library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Activities library.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# Private library
rm -f %{buildroot}%{_libdir}/libkactivitymanagerd_plugin.so

%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_bindir}/kactivitymanagerd
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_libdir}/qt5/plugins/kactivitymanagerd/*/*.so
%{_libdir}/qt5/plugins/kactivitymanagerd_fileitem_linking_plugin.so
%{_libdir}/qt5/plugins/kcm_activities.so
%{_libdir}/qt5/plugins/kio_activities.so
%{_datadir}/kf5/kactivitymanagerd
%{_libdir}/qt5/qml/org/kde/activities

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/KF5/KActivities
%{_includedir}/KF5/kactivities_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/pkgconfig/*
