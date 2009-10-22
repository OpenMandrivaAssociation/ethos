%define name ethos
%define version 0.2.2
%define release %mkrel 1
%define major 0
%define api_level 1.0
%define libname %mklibname %{name}_ %{major}
%define libuiname %mklibname %{name}ui_ %{major}
%define develname %mklibname %{name} -d

Summary: Plugin framework for GLib
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: LGPLv2
Group: System/Libraries
Url: http://git.dronelabs.com/ethos/about/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: gtk2-devel
BuildRequires: gjs-devel
BuildRequires: python-devel
BuildRequires: pygtk2.0-devel
BuildRequires: vala-devel
BuildRequires: vala-tools
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel
BuildRequires: gir-repository

BuildRequires: libtool

%description
Ethos is a plugin framework that is written in C using the GLib and GObject 
libraries. The goal is to have a single framework for applications that lower 
the barrier to entry for extensions. To enable as many communities as possible, 
various language bindings are provided to allow extensions in the language of 
choice.

Ethos includes a GUI library as well named libethos-ui. This library provides 
a gtk+ widget for managing plugins within your application. Typically, you can 
simply add this to a "Plugins" tab in your applications preferences dialog.

%package -n %{libname}
Summary: Libraries for %{name}
Group: System/Libraries

%description -n %{libname}
Libraries for the %{name} Ethos plugin framework.

%package -n %{libuiname}
Summary: Graphic libraries for %{name}
Group: System/Libraries

%description -n %{libuiname}
Graphic libraries for the %{name} Ethos plugin framework.
Requires: %{libname} = %{version}-%{release}

%package -n %{develname}
Summary: Development package for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Requires: %{libuiname} = %{version}-%{release}
Provides: %{name}-devel

%description -n %{develname}
Files for development with %{name}.

%package docs
Summary: Documentation for %{name}
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
BuildArch: noarch

%description docs
Documentation for development with %{name}.

%package python
Summary: Python bindings for %{name}
Group: Development/Python
Requires: %{libname} = %{version}-%{release}

%description python
Python bindings for development with %{name}.

%prep
%setup -q
./autogen.sh

%build
%configure --enable-introspection --enable-python --enable-gtk-doc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc COPYING AUTHORS README NEWS
%{_libdir}/libethos-%{api_level}.so.*
%{_libdir}/ethos
%{_libdir}/girepository-1.0/Ethos-%{api_level}.typelib

%files -n %{libuiname}
%defattr(-,root,root,-)
%{_libdir}/libethos-ui-%{api_level}.so.*
%{_datadir}/ethos

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/ethos-%{api_level}
%{_libdir}/pkgconfig/ethos*-%{api_level}.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Ethos-%{api_level}.gir
%{_datadir}/vala/vapi/ethos-%{api_level}.vapi
%{_datadir}/vala/vapi/ethos-ui-%{api_level}.vapi

%files docs
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/ethos

%files python
%defattr(-,root,root,-)
%{_libdir}/python2.6/site-packages/gtk-2.0/_ethos.so
%{_libdir}/python2.6/site-packages/gtk-2.0/_ethosui.so
%{_libdir}/python2.6/site-packages/gtk-2.0/ethos/
%{_datadir}/pygtk/2.0/defs/ethos.defs
%{_datadir}/pygtk/2.0/defs/ethosui.defs
