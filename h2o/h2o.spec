Summary: 	H2O - The optimized HTTP/1, HTTP/2 server
Name: 		h2o
Version: 	1.2.0
Release: 	2%{?dist}
License: 	MIT
Group:		System Environment/Daemons
Source: 	https://github.com/h2o/h2o/archive/v%{version}.tar.gz
Url: 		https://h2o.github.io/
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	cmake
Requires:	perl-Server-Starter, openssl
Source1: 	h2o.conf
Source2: 	index.html

%description
H2O is a very fast HTTP server written in C. It can also be used as a library.

%prep
%setup -q

%build
%cmake -DWITH_BUNDLED_SSL=on .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

install -p -d -m 0755 %{buildroot}/etc/h2o
install -p -d -m 0755 %{buildroot}/var/log/h2o
install -p -d -m 0755 %{buildroot}/var/www

install -p -m 0644 %{SOURCE1} %{buildroot}/etc/h2o/h2o.conf
install -p -m 0644 %{SOURCE2} %{buildroot}/var/www/index.html

%check
ctest -V %{?_smp_mflags}

%files
%defattr(-,root,root)
%config(noreplace) /etc/h2o/h2o.conf
%config(noreplace) /var/www/index.html
%{_bindir}/h2o
/usr/share/h2o/fetch-ocsp-response
/usr/share/h2o/start_server
%attr(755,nobody,nobody) %dir /var/log/h2o
%dir /var/www

%changelog
* Tue May 19 2015 Arnoud Vermeer <a.vermeer@tech.leaseweb.com> 1.2.0-2
- Working package (a.vermeer@tech.leaseweb.com)

* Tue May 19 2015 Arnoud Vermeer <a.vermeer@tech.leaseweb.com> 1.2.0-1
- new package built with tito

