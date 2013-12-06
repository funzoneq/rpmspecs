Summary: 	Secure, unlimited file-syncing. No cloud required.
Name: 		btsync
Version: 	1.2.82
Release: 	0%{?dist}
License: 	GPL
Group:		Applications/System
Source: 	http://download-lb.utorrent.com/endpoint/btsync/os/linux-glibc23-x64/track/stable
Url: 	  	http://www.bittorrent.com/sync
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
BitTorrent Sync by BitTorrent, Inc is a proprietary peer-to-peer file synchronization tool available for Windows, Mac, Linux, Android, iOS and BSD. It can sync files between devices on a local network, or between remote devices over the Internet via secure, distributed P2P technology.

%prep
%setup -n btsync_glibc23_x64

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --includedir=%{_includedir} --enable-ztex --enable-bitforce --enable-icarus --enable-cpumining

%install
rm -rf $RPM_BUILD_ROOT/*
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)

%changelog
* Sun Mar 24 2013 Arnoud Vermeer <rpms@freshway.biz> 3.0.2-0
- Initial packaging
