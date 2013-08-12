%global python26_sitelib /usr/lib/python2.6/site-packages

Summary: CouchPotato Server
Name: couchpotato
Version: 2.1.0
Release: 2%{?dist}
License: Python license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Url: https://github.com/RuudBurger/CouchPotatoServer
BuildRequires: python-devel
Requires: python >= 2.6
Source0: CouchPotatoServer-master.zip
Source1: couchpotato.sysconfig
AutoReq: no

%description
The ultimate PVR application that searches for and manages your TV shows

%prep
%setup -n CouchPotatoServer-master

%build

%install
rm -rf $RPM_BUILD_ROOT/*
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/couchpotato
install -D -m 755 init/fedora $RPM_BUILD_ROOT/etc/init.d/couchpotato
mkdir -p $RPM_BUILD_ROOT/opt/couchpotato
mv * $RPM_BUILD_ROOT/opt/couchpotato

%pre
/usr/sbin/groupadd -r -g 453 couchpotato > /dev/null 2>&1 || :
/usr/sbin/useradd  -r -g 453 -s /sbin/nologin -d /opt/couchpotato -M -c 'CouchPotato Server' -g couchpotato > /dev/null 2>&1 || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/couchpotato/*
/etc/init.d/couchpotato
%config(noreplace) /etc/sysconfig/couchpotato

%changelog
* Wed Aug 07 2013 Arnoud Vermeer <a.vermeer@freshway.biz> 2.1.0-2
- Found a version number (a.vermeer@freshway.biz)

* Wed Aug 07 2013 Arnoud Vermeer <a.vermeer@freshway.biz> fc8db130e02b8b6475a95e6725dc5dfa4926c645-1
- new package built with tito

