Summary: 	A bitcoin miner
Name: 		bfgminer
Version: 	3.6.0
Release: 	1%{?dist}
License: 	GPL
Group:		Applications/System
Source: 	http://luke.dashjr.org/programs/bitcoin/files/bfgminer/%{version}/bfgminer-%{version}.zip
Url: 		https://bitcointalk.org/?topic=78192
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	autoconf, automake, libtool, jansson-devel, git, libcurl-devel
BuildRequires:	libusb1-devel, libudev-devel, yasm-devel, ncurses-devel, uthash-devel

%description
This is a multi-threaded multi-pool GPU, FPGA and CPU miner with ATI GPU
monitoring, (over)clocking and fanspeed support for bitcoin and derivative
coins.

%prep
%setup -n bfgminer-%{version}


%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --includedir=%{_includedir} --enable-ztex --enable-bitforce --enable-icarus --enable-cpumining

%install
rm -rf $RPM_BUILD_ROOT/*
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
%{_bindir}/bfgminer
%{_bindir}/bfgminer-rpc
%{_bindir}/bitforce-firmware-flash
%{_includedir}/libblkmaker-0.1/blkmaker.h
%{_includedir}/libblkmaker-0.1/blktemplate.h
%{_includedir}/libblkmaker-0.1/blkmaker_jansson.h
%{_libdir}/libblkmaker-0.1.la
%{_libdir}/libblkmaker-0.1.so*
%{_libdir}/libblkmaker_jansson-0.1.la
%{_libdir}/libblkmaker_jansson*.so*
%{_libdir}/pkgconfig/libblkmaker_jansson-0.1.pc
%{_doc}/bfgminer/AUTHORS
%{_doc}/bfgminer/COPYING
%{_doc}/bfgminer/HACKING
%{_doc}/bfgminer/NEWS
%{_doc}/bfgminer/README
%{_doc}/bfgminer/README.ASIC
%{_doc}/bfgminer/README.FPGA
%{_doc}/bfgminer/README.RPC
%{_doc}/bfgminer/example.conf
%{_doc}/bfgminer/rpc-examples/api-example.c
%{_doc}/bfgminer/rpc-examples/api-example.php
%{_doc}/bfgminer/rpc-examples/api-example.py
%{_doc}/bfgminer/rpc-examples/api-example.pyc
%{_doc}/bfgminer/rpc-examples/api-example.pyo
%{_doc}/bfgminer/rpc-examples/miner.php

%changelog
* Tue Nov 26 2013 Arnoud Vermeer <a.vermeer@freshway.biz> 3.6.0-1
- Version bump

* Sun Jun 02 2013 Arnoud Vermeer <rpms@freshway.biz> 3.0.2-1
- Now with the latest 3.0.2 release

* Sun Mar 24 2013 Arnoud Vermeer <rpms@freshway.biz> 3.0.2-0
- Initial packaging
