Summary: 	    RedBlack Balanced Tree Searching and Sorting Library
Name: 		    libredblack
Version: 	    1.3.0
Release: 	    3%{?dist}
License: 	    Proprietary
Group:		    Applications/System
Source: 	    https://sourceforge.net/projects/libredblack/files/libredblack/1.3/libredblack-1.3.tar.gz/download/libredblack-%{version}.tar.gz
Url: 	  	    http://libredblack.sourceforge.net/
BuildRoot:  	    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python

%package devel
Summary: Additional files and headers required to compile programs using libredblack
Group: Development/Libraries
Requires: %{name} = %{version}

%description
This implements the redblack balanced tree algorithm.

%description devel
To develop programs based upon the libredblack library, the system needs to
have these header and object files available for creating the executables.
Also provides a code generator for producing custom versions of the library
tailored for particular item data types.

%prep
%setup

%build
%configure
CFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%{_libdir}/libredblack.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_libdir}/*a
%{_prefix}/share/libredblack/*
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*
%doc example.c
%doc example1.c
%doc example2.c
%doc example3.c
%doc example4.rb

%changelog
* Tue Feb 12 2019 Arnoud Vermeer <a.vermeer@freshway.biz> 1.3.0-3
- Standardize build 

* Tue Feb 12 2019 Arnoud Vermeer <a.vermeer@freshway.biz> 1.3.0-2
- Initial checkin (a.vermeer@freshway.biz)

* Tue Feb 12 2019 Arnoud Vermeer <a.vermeer@freshway.biz> 1.3.0-1
- new package built with tito
