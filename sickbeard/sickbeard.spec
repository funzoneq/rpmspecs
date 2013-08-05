%global python26_sitelib /usr/lib/python2.6/site-packages

Summary: Sick Beard
Name: sickbeard
Version: 498
Release: 0%{?dist}
Source0: Sick-Beard-master.zip
License: Python license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Url: https://github.com/midgetspy/Sick-Beard
BuildRequires: python-devel
Requires: python >= 2.6
Requires: python-cheetah

%description
The ultimate PVR application that searches for and manages your TV shows

%prep
%setup -n Sick-Beard-master

%build

%install
rm -rf $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/opt/sickbeard $RPM_BUILD_ROOT/etc/init.d
mv init.fedora $RPM_BUILD_ROOT/etc/init.d/sickbeard
mv * $RPM_BUILD_ROOT/opt/sickbeard

%pre
/usr/sbin/groupadd -r -g 453 sickbeard > /dev/null 2>&1 || :
/usr/sbin/useradd  -r -g 453 -s /sbin/nologin -d /home/sickbeard -M -c 'Sick Beard server' -g sickbeard > /dev/null 2>&1 || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/sickbeard/*
/etc/init.d/sickbeard

%changelog
