#
# spec file for package supportutils-plugin-nclient (Version 1.0-1)
#
# Copyright (C) 2010 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-nclient
URL:          https://code.google.com/p/supportutils-plugin-nclient/
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      1.0
Release:      0.DEV.20101104.3
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for the Novell Client for Linux
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     novell-client
Requires:     supportconfig-plugin-resource
Requires:     supportconfig-plugin-tag

%description
Extends supportconfig functionality to include system information about the
Novell Client for Linux. The supportconfig saves the plugin output to plugin-ncl.txt.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-nclient/issues/list

Authors:
--------
    Jeremy Meldrum <jmeldrum@novell.com>
    Jason Record <jrecord@novell.com>

%prep
%setup -q
%build
gzip -9f nclient-plugin.8
gzip -9f nClientInfo.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -d $RPM_BUILD_ROOT/sbin
install -d $RPM_BUILD_ROOT/etc/opt/novell/nclient-plugin
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0544 ncl $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -m 0544 nClientInfo $RPM_BUILD_ROOT/sbin
install -m 0600 nclient-plugin.conf $RPM_BUILD_ROOT/etc/opt/novell/nclient-plugin
install -m 0644 nclient-plugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/nclient-plugin.8.gz
install -m 0644 nClientInfo.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/nClientInfo.8.gz

%files
%defattr(-,root,root)
/usr/lib/supportconfig
/usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/ncl
/sbin/nClientInfo
/etc/opt/novell
%attr(700,root,root) /etc/opt/novell/nclient-plugin
%verify(mode) %attr(600,root,root) %config /etc/opt/novell/nclient-plugin/nclient-plugin.conf
/usr/share/man/man8/nclient-plugin.8.gz
/usr/share/man/man8/nClientInfo.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-nclient

