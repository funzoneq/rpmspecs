Name: libyang
Version: 0.16
Release: r3
Summary: Libyang library
Url: https://github.com/CESNET/libyang
Source: https://github.com/CESNET/libyang/archive/libyang-%{version}-%{release}.tar.gz
License: BSD-3-Clause
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: pcre
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: pcre-devel
BuildRequires: valgrind
BuildRequires: libcmocka-devel
BuildRequires: gcc
BuildRequires: bison
BuildRequires: flex

%package devel
Summary:    Headers of libyang library
Requires:   %{name} = %{version}-%{release}
Requires:   pcre-devel

%description devel
Headers of libyang library.

%description
Libyang is YANG data modelling language parser and toolkit written (and providing API) in C.

%prep
%setup -n libyang-%{version}-%{release}

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -D CMAKE_BUILD_TYPE:String="Package" .
make

%check
ctest --output-on-failure

%install
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/yanglint
%{_bindir}/yangre
%{_datadir}/man/man1/yanglint.1.gz
%{_libdir}/libyang.so.*
%dir %{_libdir}/libyang/
%{_mandir}/man1/yangre.1.gz

%files devel
%defattr(-,root,root)
%{_libdir}/libyang.so
%{_libdir}/pkgconfig/libyang.pc
%{_libdir}/libyang/extensions/metadata.so
%{_libdir}/libyang/extensions/nacm.so
%{_libdir}/libyang/extensions/yangdata.so
%{_libdir}/libyang/user_types/user_date_and_time.so
%{_includedir}/libyang/*

%dir %{_includedir}/libyang/

%changelog
* Tue Feb 12 2019 Arnoud Vermeer <a.vermeer@freshway.biz> 0.16-r3
- version 0.16-r3

* Thu May 31 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.81
- data tree BUGFIX update set number in ly_set_merge (Olivier Matz)


* Thu Apr 12 2018  Radek Krejci <rkrejci@cesnet.cz> 0.14.80
- schema BUGFIX remove statement with no effect (Radek Krejci)


* Mon Apr 09 2018  Radek Krejci <rkrejci@cesnet.cz> 0.14.79


* Mon Mar 19 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.78
- printer BUGFIX enforce an order on devs apply/remove (Michal Vasko)


* Mon Mar 19 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.77
- context BUGFIX removing augs/devs (Michal Vasko)
- resolve BUGFIX wrong printed variable (Michal Vasko)
- resolve BUGFIX data unres trusted resolve (Michal Vasko)


* Fri Mar 16 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.75
- data tree BUGFIX check when even with trusted flag (Michal Vasko)


* Thu Mar 15 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.74
- xpath CHANGE some tokens can be longer than 255 characters (Michal Vasko)


* Mon Mar 12 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.73
- resolve BUGFIX properly restore state for next augment search (Michal Vasko)


* Fri Mar 09 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.72
- data tree BUGFIX check uses and choice if-features when creating defaults (Michal Vasko)
- parser BUGFIX leaf(-list) in grouping type default check (Michal Vasko)


* Fri Feb 23 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.70
- resolve BUGFIX missing string pointer dereference (Michal Vasko)


* Thu Feb 15 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.69
- parser BUGFIX explicit context passing (Michal Vasko)


* Thu Feb 08 2018  Radek Krejci <rkrejci@cesnet.cz> 0.14.68
- XML printer BUGFIX printing namespaces of the data in anydata nodes (Radek Krejci)


* Thu Feb 01 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.67
- resolve CHANGE make schema nodeid "." and "*" match all namespaces (Michal Vasko)
- resolve BUGFIX relative schema ndoeid used start node as sibling (Michal Vasko)


* Thu Jan 25 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.66
- common BUGFIX do not copy quotes twice (Michal Vasko)


* Tue Jan 23 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.65
- data tree BUGFIX memory leak (Michal Vasko)


* Tue Jan 23 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.64
- common CHANGE handle nested xpaths (Michal Vasko)


* Mon Jan 22 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.63
- schema tree BUGFIX wrong parameters of unres (Michal Vasko)


* Fri Jan 19 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.62
- xml parser CHANGE error message invalid text content improved (Michal Vasko)


* Tue Jan 16 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.61
- parsers BUGFIX memory-leaked submodule (Michal Vasko)
- parsers BUGFIX invalid reads of freed memory (Michal Vasko)


* Mon Jan 15 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.60
- info printer BUGFIX enumeration derived type segfault (Michal Vasko)
- travis CHANGE osx no longer needs pcre upgrade (Michal Vasko)


* Fri Jan 12 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.59
- CHANGE use correct schema node for leaf default check (Michal Vasko)


* Thu Jan 11 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.57
- CHANGE unify loading schemas and do not duplicate code (Michal Vasko)
- tests BUGFIX error codes changed (Michal Vasko)


* Wed Jan 03 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.56
- tests BUGFIX error codes changed (Michal Vasko)
- xml CHANGE handle special "xml" attribute namespace (Michal Vasko)
- parser BUGFIX inaccurate error codes fixed (Michal Vasko)


* Wed Jan 03 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.55
- schema tree BUGFIX unsupported deviation of a node under uses (Michal Vasko)


* Tue Jan 02 2018  Michal Vasko <mvasko@cesnet.cz> 0.14.54
- json parser BUGFIX accept empty data (Michal Vasko)


* Thu Dec 14 2017  Michal Vasko <mvasko@cesnet.cz> 0.14.53
- schema tree BUGFIX removing not-supported deviation from augment (Michal Vasko)
- context BUGFIX initialize thread-local ctx in api functions (Michal Vasko)


* Wed Dec 13 2017  Michal Vasko <mvasko@cesnet.cz> 0.14.52
- tests CHANGE context tests added and improved (Michal Vasko)
- yang parser BUGFIX double free (Michal Vasko)
- context BUGFIX yang-library data tree changed (Michal Vasko)
- doc BUGFIX path to the generated libyang.h in doxygen config (Radek Krejci)
- fixup! tests CHANGE use foreign identity (Michal Vasko)
- tests CHANGE use foreign identity (Michal Vasko)


* Tue Dec 12 2017  Michal Vasko <mvasko@cesnet.cz> 0.14.51
- common BUGFIX always check that xpath does not end prematurely (Michal Vasko)


* Thu Dec 07 2017  Michal Vasko <mvasko@cesnet.cz> 0.14.50
- common CHANGE use data callback when transforming paths (Michal Vasko)
- fixup! parser & printer CHANGE xpath1.0 type correct handling (Michal Vasko)
- parser & printer CHANGE xpath1.0 type correct handling (Michal Vasko)
- data tree CHANGE new function lyd_set_merge (Michal Vasko)
- data tree BUGFIX parsed operation could get deleted by false when (Michal Vasko)
- data tree BUGFIX typo (Michal Vasko)


* Tue Nov 21 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.88
- resolve BUGFIX add missing warning messages (Michal Vasko)
- resolve BUGFIX detect unresolved augment also in non-implemented modules (Michal Vasko)


* Wed Nov 15 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.87
- data tree BUGFIX possible illegal pointer cleared (Michal Vasko)


* Mon Nov 13 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.86
- xpath BUGFIX special * path is not limited to context module (Michal Vasko)
- xpath BUGFIX all namespace internal expression logic was wrong (Michal Vasko)


* Fri Nov 10 2017  Radek Krejci <rkrejci@cesnet.cz> 0.13.84
- schema parsers BUGFIX replacing type by deviation (Radek Krejci)
- XML data parser BUGFIX with LYD_OPT_STRICT check that non-terminal nodes does not contain text data (Radek Krejci)


* Mon Nov 06 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.81
- parser BUGFIX dollar signs in patterns must be escaped for pcre (Michal Vasko)


* Thu Nov 02 2017  Radek Krejci <rkrejci@cesnet.cz> 0.13.80
- YANG parser CHANGE ommit module parse fail message when parsing submodule file (Radek Krejci)


* Mon Oct 30 2017  Radek Krejci <rkrejci@cesnet.cz> 0.13.79
- schema parsers BUGFIX path of the node affected by status inconsistency (Radek Krejci)


* Fri Oct 27 2017  Radek Krejci <rkrejci@cesnet.cz> 0.13.78
- yanglint CHANGE support JSON in rpcreply data file (Radek Krejci)
- JSON parser BUGFIX parsing reply data in JSON format (Radek Krejci)
- JSON parser BUGFIX double free (Radek Krejci)


* Fri Oct 27 2017  Radek Krejci <rkrejci@cesnet.cz> 0.13.77
- schema parsers BUGFIX NULL pointer dereference (Radek Krejci)
- extensions BUGFIX searching for extension plugins (Radek Krejci)
- schema parsers CHANGE resolving uses's augments (Radek Krejci)
- schema parsers BUGFIX checking identityref values in XPaths (Radek Krejci)
- schema parsers BUGFIX handle duplicities in unresolved items (Radek Krejci)
- xpath BUGFIX parse the predicate even if there are no nodes for evaluation (Michal Vasko)


* Fri Oct 06 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.75
- data tree BUGFIX check return value of lyp_parse_value (Michal Vasko)
- resolve CHANGE use data callback for unresolved data identityref values (Michal Vasko)


* Tue Oct 03 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.74
- resolve BUGFIX compare instid values on canonical values (Michal Vasko)
- resolve BUGFIX do not print internal errors on syntactic ones (Michal Vasko)
- xpath CHANGE warnings enhanced and unified (Michal Vasko)
- log CHANGE special hide value 255 makes warnings from errors (Michal Vasko)
- resolve CHANGE print message about identity in a non-implemented module (Michal Vasko)


* Mon Oct 02 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.72
- resolve BUGFIX unintialized variable warning (Michal Vasko)
- resolve BUGFIX use character count from successful parsing (Michal Vasko)
- libyang CHANGE building paths of arbitrary length (Michal Vasko)


* Tue Sep 26 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.69
- data tree BUGFIX invalid free in merge (Michal Vasko)


* Fri Sep 22 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.68
- yanglint FEATURE history saving (Michal Vasko)


* Thu Sep 21 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.67
- resolve BUGFIX check leafref if-features after making modules implemented (Michal Vasko)
- log CHANGE print information about module implemented status (Michal Vasko)
- test CHANGE augment leafref if-feature test also for yin (Michal Vasko)


* Tue Sep 19 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.66
- xpath BUGFIX handle unions in type checks (Michal Vasko)
- xpath BUGFIX typo (Michal Vasko)
- xpath CHANGE count function accepts leaf-list or nodes with list parents nodes (Michal Vasko)
- xpath CHANGE for strings accept any leaf/leaf-list of string-type (Michal Vasko)
- resolve BUGFIX identityref value can be specified with module name (Michal Vasko)


* Fri Sep 15 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.63
- resolve BUGFIX remove invalid restriction of intid keys order (Michal Vasko)


* Thu Sep 14 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.62
- libyang CHANGE allow ctx to be NULL and read from another parameter (Michal Vasko)
- log BUGFIX memory leak (Radek Krejci)
- log BUGFIX check boundaries of the buffer to store log messages (Radek Krejci)
- schema tree BUGFIX refining if-feature (Radek Krejci)
- schema tree BUGFIX memory leak (Radek Krejci)
- tests CHANGE set MALLOC_CHECK_=3 for all (non-valgrind) tests (Radek Krejci)
- schema tree CHANGE check for arrays size limitations (Radek Krejci)


* Wed Sep 13 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.54
- info printer BUGFIX properly restrict return node types (Michal Vasko)
- travis CHANGE upgrade pcre in OSX (Radek Krejci)


* Thu Sep 07 2017  Radek Krejci <rkrejci@cesnet.cz> 0.13.53
- travis CHANGE upgrade pcre in OSX (Radek Krejci)
- travis CHANGE do not use valgrind on MacOS X (Radek Krejci)
- schema parsers CHANGE status inheritance in uses (Radek Krejci)
- parser yang CHANGE better checking and inheritence of status (PavolVican)
- tests BUGFIX add forgotten status test source file (Radek Krejci)
- schema parsers CHANGE better checking and inheritence of status (Radek Krejci)
- log BUGFIX provide prefix on top-level nodes (Radek Krejci)
- schema parsers BUGFIX use of uninitialized memory (Radek Krejci)
- xml parser BUGFIX restore previous parser's context in thread-specific variable (Radek Krejci)
- xpath BUGFIX too small flags member of restrictions structure (when, must) (Radek Krejci)
- context CHANGE storing parser's error messages (Radek Krejci)
- yanglint CHANGE remove unused header file (Radek Krejci)


* Fri Aug 25 2017  Radek Krejci <rkrejci@cesnet.cz> 0.13.49
- schema parsers BUGFIX handling deviated augments (Radek Krejci)
- schema parsers BUGFIX memory leak (Radek Krejci)
- YANG parser BUGFIX add missing hack for deviated nodes from augments (Radek Krejci)


* Tue Aug 22 2017  Radek Krejci <rkrejci@cesnet.cz> 0.13.47
- data parsers BUGFIX empty value for bits built-in type (Radek Krejci)


* Fri Aug 18 2017  Radek Krejci <rkrejci@cesnet.cz> 0.13.46
- trees BUGFIX use __typeof__ instead of typeof (Radek Krejci)
- libyang CHANGE use compiler thread-local variables (Michal Vasko)


* Thu Aug 17 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.44
- test BUGFIX invalid xpath should not cause an error (Michal Vasko)
- xpath CHANGE check xpath function arguments and operator operands (Michal Vasko)


* Mon Aug 14 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.43
- fixup! resolve BUGFIX do not delete false when data when not possible to check when (Michal Vasko)


* Mon Aug 14 2017  Michal Vasko <mvasko@cesnet.cz> 0.13.42
- fixup! resolve BUGFIX do not delete false when data when not possible to check when (Michal Vasko)
- fixup! resolve BUGFIX do not delete false when data when not possible to check when (Michal Vasko)
- schema tree CHANGE add xpath_dep flags for specific msut and when also (Michal Vasko)
- resolve BUGFIX do not delete false when data when not possible to check when (Michal Vasko)
- parser CHANGE LYD_OPT_NOAUTODEL flag allowed for operations too (Michal Vasko)
- fixup! schema tree BUGFIX lys_child() on leaf/leaflist (Michal Vasko)
- data parser BUGFIX conversion from JSON to XML path format (Radek Krejci)
- data parsers BUGFIX checking binary's base64 format (Radek Krejci)
- JSON parser BUGFIX handling LYD_OPT_DATA_ADD_YANGLIB option on empty JSON data (Radek Krejci)
- context BUGFIX memory leaks (Radek Krejci)
- yangre BUGFIX memory leaks (Radek Krejci)
- schema parsers BUGFIX remove dead code (Radek Krejci)
- schema parsers BUGFIX incomplete realloc() (Radek Krejci)
- schema parsers CHANGE simplify conditions (Radek Krejci)
- schema tree BUGFIX lys_child() on leaf/leaflist (Radek Krejci)
- data parsers BUGFIX checking Base64 (Radek Krejci)
- data parsers CHANGE strict Base64 content checking (Radek Krejci)
- yanglint CHANGE handle parsing empty RPC reply (Radek Krejci)
- XML parser BUGFIX parsing empty data as RPC, Reply or Notification (Radek Krejci)
- yanglint FEATURE print list of the loaded schemas in non-interactive mode (Radek Krejci)
- yanglint FEATURE allow merging input data file (Radek Krejci)
- build BUGFIX typo (Radek Krejci)


* Mon Aug 07 2017  Radek Krejci <rkrejci@cesnet.cz> 0.12.203
- data parser BUGFIX negative values of unsigned integers (Radek Krejci)


* Mon Aug 07 2017  Michal Vasko <mvasko@cesnet.cz> 0.12.202
- resolve BUGFIX decimal64 parsing overflow (Michal Vasko)


* Thu Aug 03 2017  Radek Krejci <rkrejci@cesnet.cz> 0.12.201
- yanglint BUGFIX logic for data parser option combined with schema output warning (Radek Krejci)
- BUGFIX handling negative decimal64 values (mohitarora24)


* Wed Aug 02 2017  Radek Krejci <rkrejci@cesnet.cz> 0.12.200
- BUGFIX handling negative decimal64 values (mohitarora24)


* Tue Jul 11 2017  Michal Vasko <mvasko@cesnet.cz> 0.12.199
- xpath BUGFIX support for xpath length 256 and more (Michal Vasko)


* Tue Jul 11 2017  Radek Krejci <rkrejci@cesnet.cz> 0.12.198
- schema parsers BUGFIX parsing range values on 32b system (Radek Krejci)
- fixup! resolve BUGFIX augment path nodes do not inherit prefixes from parent (Michal Vasko)
- resolve BUGFIX augment path nodes do not inherit prefixes from parent (Michal Vasko)
- schema parsers BUGFIX remove invalid assert (Radek Krejci)
- tree parsers BUGFIX NULL dereference in extensions processing (Radek Krejci)
- Revert "resolve BUGFIX augment path nodes do not inherit prefixes from parent" (Radek Krejci)
- resolve BUGFIX augment path nodes do not inherit prefixes from parent (Michal Vasko)


* Tue Jul 04 2017  Michal Vasko <mvasko@cesnet.cz> 0.12.194
- resolve BUGFIX another batch of xpath prefix fixes (Michal Vasko)


* Tue Jul 04 2017  Radek Krejci <rkrejci@cesnet.cz> 0.12.193
- CHANGE print warning when a module is imported multiple times with different prefixes (Radek Krejci)
- yanglint CHANGE use context node from the data (Michal Vasko)
- xpath BUGFIX proper predicate end searching (Michal Vasko)
- xpath BUGFIX unprefixed nodes module (Michal Vasko)
- xpath CHANGE use proper context node for error messages (Michal Vasko)
- xpath CHANGE do not print internal errors on invalid modules (Michal Vasko)


* Mon Jul 03 2017  Radek Krejci <rkrejci@cesnet.cz> 0.12.191
- BUGFIX dereferencing NULL pointer (Radek Krejci)


* Fri Jun 30 2017  Michal Vasko <mvasko@cesnet.cz> 0.12.190
- xpath BUGFIX proper node module checking (Michal Vasko)
- CHANGE improve checking for memory allocation errors (Radek Krejci)
- resolve CHANGE copy leafrefs in unions in typedefs (Michal Vasko)


* Tue Jun 27 2017  Michal Vasko <mvasko@cesnet.cz> 0.12.187
- fixup! BUGFIX positional xpath arguments evaluate on child axis (Michal Vasko)
- BUGFIX positional xpath arguments evaluate on child axis (Michal Vasko)


* Mon Jun 12 2017  Michal Vasko <mvasko@cesnet.cz> 0.12.185
- resolve BUGFIX resolving augments more times is legal (Michal Vasko)
- docs CHANGE add information about binary packages (Radek Krejci)
- packages BUGFIX dependencies (PavolVican)
- CHANGE CMakeList check build dependency (PavolVican)
- packages BUGFIX remove unused files and package config (PavolVican)
- packages CHANGE add scripts for local building rpm and deb package (PavolVican)
- packages BUGFIX spec files and shell script (PavolVican)


* Thu Jun 08 2017  PavolVican <xvican01@stud.fit.vutbr.cz> 0.12.183


* Fri Jun 09 2017  Radek Krejci <rkrejci@cesnet.cz> 0.12.184
- docs CHANGE add information about binary packages (Radek Krejci)
- packages BUGFIX dependencies (PavolVican)
- CHANGE CMakeList check build dependency (PavolVican)
- packages BUGFIX remove unused files and package config (PavolVican)
- packages CHANGE add scripts for local building rpm and deb package (PavolVican)
- packages BUGFIX spec files and shell script (PavolVican)


* Thu Jun 08 2017  PavolVican <xvican01@stud.fit.vutbr.cz> 0.12.183


* Fri Jun 09 2017  Radek Krejci <rkrejci@cesnet.cz> 0.12.184
- docs CHANGE add information about binary packages (Radek Krejci)
- packages BUGFIX dependencies (PavolVican)
- CHANGE CMakeList check build dependency (PavolVican)
- packages BUGFIX remove unused files and package config (PavolVican)
- packages CHANGE add scripts for local building rpm and deb package (PavolVican)
- packages BUGFIX spec files and shell script (PavolVican)


* Thu Jun 08 2017  PavolVican <xvican01@stud.fit.vutbr.cz> 0.12.183


* Fri Jun 09 2017  Radek Krejci <rkrejci@cesnet.cz> 0.12.184
- docs CHANGE add information about binary packages (Radek Krejci)
- packages BUGFIX dependencies (PavolVican)
- CHANGE CMakeList check build dependency (PavolVican)
- packages BUGFIX remove unused files and package config (PavolVican)
- packages CHANGE add scripts for local building rpm and deb package (PavolVican)
- packages BUGFIX spec files and shell script (PavolVican)


* Mon May 29 2017  PavolVican <xvican01@stud.fit.vutbr.cz> 0.12.183
- packages BUGFIX spec files and shell script (PavolVican)
