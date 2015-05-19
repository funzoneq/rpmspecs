Summary: 	H2O - The optimized HTTP/1, HTTP/2 server
Name: 		h2o
Version: 	1.2.0
Release: 	1%{?dist}
License: 	MIT
Group:		System Environment/Daemons
Source: 	https://github.com/h2o/h2o/archive/v%{version}.tar.gz
Url: 		https://h2o.github.io/
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	cmake

%description
H2O is a very fast HTTP server written in C. It can also be used as a library.

%prep
%setup -c h2o-%{version}

%build
cmake -DWITH_BUNDLED_SSL=on .
make

%install
rm -rf $RPM_BUILD_ROOT/*
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)

%changelog
* Tue May 19 2015 Arnoud Vermeer <a.vermeer@tech.leaseweb.com> 1.2.0-1
- new package built with tito

