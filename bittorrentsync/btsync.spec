Summary: 	Secure, unlimited file-syncing. No cloud required.
Name: 		btsync
Version: 	1.2.82
Release: 	1%{?dist}
License: 	Proprietary
Group:		Applications/System
Source: 	http://download-lb.utorrent.com/endpoint/btsync/os/linux-glibc23-x64/track/stable
Url: 	  	http://www.bittorrent.com/sync
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
BitTorrent Sync by BitTorrent, Inc is a proprietary peer-to-peer file synchronization tool available for Windows, Mac, Linux, Android, iOS and BSD. It can sync files between devices on a local network, or between remote devices over the Internet via secure, distributed P2P technology.

%prep
%setup -n btsync_glibc23_x64

%build
# precompiled package

%install
rm -rf $RPM_BUILD_ROOT/*
install -p -d -m 0755 %{buildroot}/usr/bin
install -p -m 0755 btsync %{buildroot}/usr/bin/
install -p -m 0644 LICENSE.TXT %{buildroot}/docs/

%files
%defattr(-,root,root,-)
%{_bindir}/btsync

%changelog
* Fri Dec 06 2013 Arnoud Vermeer <a.vermeer@freshway.biz> 1.2.82-1
- new package built with tito

* Sun Mar 24 2013 Arnoud Vermeer <rpms@freshway.biz> 3.0.2-0
- Initial packaging
