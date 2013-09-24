%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Indicator plugin for the Xfce panel
Name:		xfce4-indicator-plugin
Version:	2.1.0
Release:	0
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(indicator-0.4)

%description
An indicator panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.*g
