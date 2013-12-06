Summary: 	    Secure, unlimited file-syncing. No cloud required.
Name: 		    btsync
Version: 	    1.2.82
Release: 	    3%{?dist}
License: 	    Proprietary
Group:		    Applications/System
Source: 	    http://download-lb.utorrent.com/endpoint/btsync/os/linux-glibc23-x64/track/stable/btsync_glibc23_x64.tar.gz
Url: 	  	    http://www.bittorrent.com/sync
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides: 	  libc.so.6(GLIBC_PRIVATE)(64bit)
AutoReqProv: 	no
Source0:      sample-config

%description
BitTorrent Sync by BitTorrent, Inc is a proprietary peer-to-peer file synchronization tool available for Windows, Mac, Linux, Android, iOS and BSD. It can sync files between devices on a local network, or between remote devices over the Internet via secure, distributed P2P technology.

%prep
%setup -c btsync_glibc23_x64

%build
# precompiled package

%install
rm -rf $RPM_BUILD_ROOT/*
install -p -d -m 0755 %{buildroot}/etc/btsync
install -p -d -m 0755 %{buildroot}/usr/bin

install -p -m 0644 %{SOURCE0} %{buildroot}/etc/btsync/
install -p -m 0755 btsync %{buildroot}/usr/bin/

%files
%defattr(-,root,root,-)
%doc LICENSE.TXT
%config(noreplace) /etc/btsync/sample-config
%{_bindir}/btsync

%changelog
* Fri Dec 06 2013 Arnoud Vermeer <a.vermeer@freshway.biz> 1.2.82-3
- Rename (a.vermeer@freshway.biz)

* Fri Dec 06 2013 Arnoud Vermeer <a.vermeer@freshway.biz> 1.2.82-2
- Cleanup (arnoud@tumblr.com)

* Fri Dec 06 2013 Arnoud Vermeer <a.vermeer@freshway.biz> 1.2.82-1
- new package built with tito
