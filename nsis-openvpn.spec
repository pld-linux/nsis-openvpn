Summary:	NSIS OpenVPN installer builder
Name:		nsis-openvpn
Version:	2.0.9
Release:	0.1
# OpenVPN windows executable is GPL, no ideas about the rest
License:	GPL
Group:		Development/Tools
URL:		http://openvpn.se/files/howto/openvpn-howto_roll_your_own_installation_package.html
Source0:	http://www.openvpn.se/files/install_packages_source/openvpn_install_source-2.0.9-gui-1.0.3.zip
# NoSource0-md5:	64fce7dc20fdd991ffdee2cfce9dfb0b
NoSource:	0
Requires:	nsis
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/nsis/Contrib/OpenVPN

%description
This package contains needed NSIS scripts and binaries to build
OpenVPN installer for Windows.

%prep
%setup -qc

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
