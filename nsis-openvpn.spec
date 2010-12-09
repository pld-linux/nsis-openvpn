Summary:	NSIS OpenVPN installer builder
Name:		nsis-openvpn
Version:	2.0.9
Release:	0.16
# OpenVPN windows executable is GPL, no ideas about the rest
License:	GPL
Group:		Development/Tools
URL:		http://openvpn.se/files/howto/openvpn-howto_roll_your_own_installation_package.html
Source0:	http://www.openvpn.se/files/install_packages_source/openvpn_install_source-%{version}-gui-1.0.3.zip
# NoSource0-md5:	64fce7dc20fdd991ffdee2cfce9dfb0b
NoSource:	0
Source1:	openvpn-gui.nsi
Patch1:		skip-components.patch
Patch2:		options-override.patch
Patch3:		defaults.patch
Patch4:		install-hook.patch
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unix2dos
Requires:	nsis >= 2.34
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/nsis/Contrib/OpenVPN

%description
This package contains needed NSIS scripts and binaries to build
OpenVPN installer for Windows.

%prep
%setup -qc
cp -a %{SOURCE1} openvpn-gui.nsi
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
unix2dos openvpn-gui.nsi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a . $RPM_BUILD_ROOT%{_appdir}
rm $RPM_BUILD_ROOT%{_appdir}/ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{_appdir}
