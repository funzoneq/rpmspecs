Summary: 	    RedBlack Balanced Tree Searching and Sorting Library
Name: 		    libredblack
Version: 	    1.3.0
Release: 	    3%{?dist}
License: 	    Proprietary
Group:		    Applications/System
Source: 	    https://sourceforge.net/projects/libredblack/files/libredblack/1.3/libredblack-1.3.tar.gz/download/libredblack-%{version}.tar.gz
Url: 	  	    http://libredblack.sourceforge.net/
BuildRoot:  	    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A library to provide the RedBlack balanced tree searching and sorting algorithm. The algorithm was taken from the book "Introduction to Algorithms" by Cormen, Leiserson & Rivest.

%prep
%setup -n libredblack-%{version}

%configure

%install
%make_install

%files
%defattr(-,root,root,-)

%changelog
* Tue Feb 12 2019 Arnoud Vermeer <a.vermeer@freshway.biz> 1.3.0-3
- Standardize build 

* Tue Feb 12 2019 Arnoud Vermeer <a.vermeer@freshway.biz> 1.3.0-2
- Initial checkin (a.vermeer@freshway.biz)

* Tue Feb 12 2019 Arnoud Vermeer <a.vermeer@freshway.biz> 1.3.0-1
- new package built with tito
