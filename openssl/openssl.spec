# For the curious:
# 0.9.5a soversion = 0
# 0.9.6  soversion = 1
# 0.9.6a soversion = 2
# 0.9.6c soversion = 3
# 0.9.7a soversion = 4
# 0.9.7ef soversion = 5
# 0.9.8ab soversion = 6
# 0.9.8g soversion = 7
# 0.9.8jk + EAP-FAST soversion = 8
# 1.0.0 soversion = 10
%define soversion 10

# Number of threads to spawn when testing some threading fixes.
%define thread_test_threads %{?threads:%{threads}}%{!?threads:1}

# Arches on which we need to prevent arch conflicts on opensslconf.h, must
# also be handled in opensslconf-new.h.
%define multilib_arches %{ix86} ia64 ppc %{power64} s390 s390x sparcv9 sparc64 x86_64

%define name openssl
# since el6 provides 1.0.0 we need to be a little more specfic on basever.
%define basever 1.0.1
%define real_name openssl

Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: %{name}
Version: 1.0.1g
# Do not forget to bump SHLIB_VERSION on version upgrades
Release: 0%{?dist}
# We have to remove certain patented algorithms from the openssl source
# tarball with the hobble-openssl script which is included below.
# The original openssl upstream tarball cannot be shipped in the .src.rpm.
Source: http://www.openssl.org/source/openssl-%{version}.tar.gz
Source1: hobble-openssl
Source2: Makefile.certificate
Source6: make-dummy-cert
Source8: openssl-thread-test.c
Source9: opensslconf-new.h
Source10: opensslconf-new-warning.h
Source11: README.FIPS
# Build changes
Patch1: openssl-1.0.1-beta2-rpmbuild.patch
Patch2: openssl-1.0.0f-defaults.patch
Patch4: openssl-1.0.0-beta5-enginesdir.patch
Patch5: openssl-0.9.8a-no-rpath.patch
Patch6: openssl-0.9.8b-test-use-localhost.patch
Patch7: openssl-1.0.0-timezone.patch
Patch8: openssl-1.0.1c-perlfind.patch
Patch9: openssl-1.0.1c-aliasing.patch
# Bug fixes
Patch23: openssl-1.0.0-beta4-default-paths.patch
# Functionality changes
Patch33: openssl-1.0.0-beta4-ca-dir.patch
Patch34: openssl-0.9.6-x509.patch
Patch35: openssl-0.9.8j-version-add-engines.patch
Patch36: openssl-1.0.0e-doc-noeof.patch
#Patch38: openssl-1.0.1-beta2-ssl-op-all.patch
Patch39: openssl-1.0.1c-ipv6-apps.patch
#Patch40: openssl-1.0.0-nofips.patch
Patch45: openssl-0.9.8j-env-nozlib.patch
Patch47: openssl-1.0.0-beta5-readme-warning.patch
Patch49: openssl-1.0.1a-algo-doc.patch
Patch50: openssl-1.0.1-beta2-dtls1-abi.patch
Patch51: openssl-1.0.1-version.patch
#Patch56: openssl-1.0.0c-rsa-x931.patch
#Patch58: openssl-1.0.1-beta2-fips-md5-allow.patch
Patch60: openssl-1.0.0d-apps-dgst.patch
Patch63: openssl-1.0.0d-xmpp-starttls.patch
Patch65: openssl-1.0.0e-chil-fixes.patch
Patch66: openssl-1.0.1-pkgconfig-krb5.patch
#Patch67: openssl-1.0.0-fips-pkcs8.patch
Patch68: openssl-1.0.1c-secure-getenv.patch
# Backported fixes including security fixes
Patch81: openssl-1.0.1-beta2-padlock64.patch
Patch82: openssl-1.0.1c-backports.patch

License: OpenSSL
Group: System Environment/Libraries
URL: http://www.openssl.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: coreutils, krb5-devel, perl, sed, zlib-devel, /usr/bin/cmp
BuildRequires: /usr/bin/rename
Requires: coreutils, make
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{real_name} = %{version}-%{release}
Conflicts: %{real_name} < %{basever}

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

%package libs
Summary: A general purpose cryptography library with TLS implementation
Group: System Environment/Libraries
Provides: %{real_name}-libs = %{version}-%{release}
Conflicts: %{real_name}-libs < %{basever}
Requires: ca-certificates >= 2008-5
# Needed obsoletes due to the base/lib subpackage split
# Obsoletes: openssl < 1:1.0.1-0.3.beta3

%description libs
OpenSSL is a toolkit for supporting cryptography. The openssl-libs
package contains the libraries that are used by various applications which
support cryptographic algorithms and protocols.

%package devel
Summary: Files for development of applications which will use OpenSSL
Group: Development/Libraries
Provides: %{real_name}-devel = %{version}-%{release}
Conflicts: %{real_name}-devel < %{basever}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: krb5-devel%{?_isa}, zlib-devel%{?_isa}
Requires: pkgconfig

%description devel
OpenSSL is a toolkit for supporting cryptography. The openssl-devel
package contains include files needed to develop applications which
support various cryptographic algorithms and protocols.

%package static
Summary:  Libraries for static linking of applications which will use OpenSSL
Group: Development/Libraries
Provides: %{real_name}-static = %{version}-%{release}
Conflicts: %{real_name}-static < %{basever}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
OpenSSL is a toolkit for supporting cryptography. The openssl-static
package contains static libraries needed for static linking of
applications which support various cryptographic algorithms and
protocols.

%package perl
Summary: Perl scripts provided with OpenSSL
Group: Applications/Internet
Requires: perl
Provides: %{real_name}-perl = %{version}-%{release}
Conflicts: %{real_name}-perl < %{basever}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description perl
OpenSSL is a toolkit for supporting cryptography. The openssl-perl
package provides Perl scripts for converting certificates and keys
from other formats to the formats used by the OpenSSL toolkit.

%prep
%setup -q -n %{real_name}-%{version}

# The hobble_openssl is called here redundantly, just to be sure.
# The tarball has already the sources removed.
#%{SOURCE1} > /dev/null
%patch1 -p1 -b .rpmbuild
%patch2 -p1 -b .defaults
%patch4 -p1 -b .enginesdir %{?_rawbuild}
%patch5 -p1 -b .no-rpath
%patch6 -p1 -b .use-localhost
%patch7 -p1 -b .timezone
%patch8 -p1 -b .perlfind
%patch9 -p1 -b .aliasing

%patch23 -p1 -b .default-paths

%patch33 -p1 -b .ca-dir
%patch34 -p1 -b .x509
%patch35 -p1 -b .version-add-engines
%patch36 -p1 -b .doc-noeof
#%patch38 -p1 -b .op-all
%patch39 -p1 -b .ipv6-apps
#%patch40 -p1 -b .nofips
%patch45 -p1 -b .env-nozlib
%patch47 -p1 -b .warning
%patch49 -p1 -b .algo-doc
%patch50 -p1 -b .dtls1-abi
%patch51 -p1 -b .version
#%patch56 -p1 -b .x931
#%patch58 -p1 -b .md5-allow
%patch60 -p1 -b .dgst
%patch63 -p1 -b .starttls
%patch65 -p1 -b .chil
%patch66 -p1 -b .krb5
#%patch67 -p1 -b .pkcs8
#%patch68 -p1 -b .secure-getenv

%patch81 -p1 -b .padlock64
#%patch82 -p1 -b .backports

# Modify the various perl scripts to reference perl in the right location.
perl util/perlpath.pl `dirname %{__perl}`

# Generate a table with the compile settings for my perusal.
touch Makefile
make TABLE PERL=%{__perl}

%build
# Figure out which flags we want to use.
# default
sslarch=%{_os}-%{_target_cpu}
%ifarch %ix86
sslarch=linux-elf
if ! echo %{_target} | grep -q i686 ; then
	sslflags="no-asm 386"
fi
%endif
%ifarch sparcv9
sslarch=linux-sparcv9
sslflags=no-asm
%endif
%ifarch sparc64
sslarch=linux64-sparcv9
sslflags=no-asm
%endif
%ifarch alpha alphaev56 alphaev6 alphaev67
sslarch=linux-alpha-gcc
%endif
%ifarch s390 sh3eb sh4eb
sslarch="linux-generic32 -DB_ENDIAN"
%endif
%ifarch s390x
sslarch="linux64-s390x"
%endif
%ifarch %{arm} sh3 sh4
sslarch=linux-generic32
%endif
%ifarch %{power64}
sslarch=linux-ppc64
%endif

# ia64, x86_64, ppc are OK by default
# Configure the build tree.  Override OpenSSL defaults with known-good defaults
# usable on all platforms.  The Configure script already knows to use -fPIC and
# RPM_OPT_FLAGS, so we can skip specifiying them here.
./Configure \
 	--prefix=/usr --openssldir=%{_sysconfdir}/pki/tls ${sslflags} \
 	zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
	enable-cms enable-md2 no-mdc2 no-rc5 enable-ec enable-ecdh enable-ecdsa enable-ec2m enable-ecdsa no-srp \
 	--with-krb5-flavor=MIT --enginesdir=%{_libdir}/openssl/engines \
	--with-krb5-dir=/usr shared  ${sslarch}

# Add -Wa,--noexecstack here so that libcrypto's assembler modules will be
# marked as not requiring an executable stack.
# Also add -DPURIFY to make using valgrind with openssl easier as we do not
# want to depend on the uninitialized memory as a source of entropy anyway.
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -DPURIFY"
make depend
make all

# Generate hashes for the included certs.
make rehash

# Overwrite FIPS README
cp -f %{SOURCE11} .

%check
# Verify that what was compiled actually works.

# We must revert patch33 before tests otherwise they will fail
patch -p1 -R < %{PATCH33}

LD_LIBRARY_PATH=`pwd`${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export LD_LIBRARY_PATH
make -C test apps tests
%{__cc} -o openssl-thread-test \
	`krb5-config --cflags` \
	-I./include \
	$RPM_OPT_FLAGS \
	%{SOURCE8} \
	-L. \
	-lssl -lcrypto \
	`krb5-config --libs` \
	-lpthread -lz -ldl
./openssl-thread-test --threads %{thread_test_threads}

# Add generation of HMAC checksum of the final stripped library
#%define __spec_install_post \
#    %{?__debug_package:%{__debug_install_post}} \
#    %{__arch_install_post} \
#    %{__os_install_post} \
#    crypto/fips/fips_standalone_hmac $RPM_BUILD_ROOT%{_libdir}/libcrypto.so.%{version} >$RPM_BUILD_ROOT%{_libdir}/.libcrypto.so.%{version}.hmac \
#    ln -sf .libcrypto.so.%{version}.hmac $RPM_BUILD_ROOT%{_libdir}/.libcrypto.so.%{soversion}.hmac \
#    crypto/fips/fips_standalone_hmac $RPM_BUILD_ROOT%{_libdir}/libssl.so.%{version} >$RPM_BUILD_ROOT%{_libdir}/.libssl.so.%{version}.hmac \
#    ln -sf .libssl.so.%{version}.hmac $RPM_BUILD_ROOT%{_libdir}/.libssl.so.%{soversion}.hmac \
#%{nil}

%define __provides_exclude_from %{_libdir}/openssl

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
# Install OpenSSL.
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_mandir},%{_libdir}/openssl}
make INSTALL_PREFIX=$RPM_BUILD_ROOT install
make INSTALL_PREFIX=$RPM_BUILD_ROOT install_docs
mv $RPM_BUILD_ROOT%{_libdir}/engines $RPM_BUILD_ROOT%{_libdir}/openssl
mv $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/man/* $RPM_BUILD_ROOT%{_mandir}/
rmdir $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/man
rename so.%{soversion} so.%{version} $RPM_BUILD_ROOT%{_libdir}/*.so.%{soversion}
mkdir $RPM_BUILD_ROOT/%{_lib}
for lib in $RPM_BUILD_ROOT%{_libdir}/*.so.%{version} ; do
	chmod 755 ${lib}
	ln -s -f `basename ${lib}` $RPM_BUILD_ROOT%{_libdir}/`basename ${lib} .%{version}`
	ln -s -f `basename ${lib}` $RPM_BUILD_ROOT%{_libdir}/`basename ${lib} .%{version}`.%{soversion}
done

# Install a makefile for generating keys and self-signed certs, and a script
# for generating them on the fly.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/certs
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/certs/Makefile
install -m755 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/certs/make-dummy-cert

# Make sure we actually include the headers we built against.
for header in $RPM_BUILD_ROOT%{_includedir}/openssl/* ; do
	if [ -f ${header} -a -f include/openssl/$(basename ${header}) ] ; then
		install -m644 include/openssl/`basename ${header}` ${header}
	fi
done

# Rename man pages so that they don't conflict with other system man pages.
pushd $RPM_BUILD_ROOT%{_mandir}
for manpage in man*/* ; do
	if [ -L ${manpage} ]; then
		TARGET=`ls -l ${manpage} | awk '{ print $NF }'`
		ln -snf ${TARGET}ssl ${manpage}ssl
		rm -f ${manpage}
	else
		mv ${manpage} ${manpage}ssl
	fi
done
for conflict in passwd rand ; do
	rename ${conflict} ssl${conflict} man*/${conflict}*
done
popd

# Pick a CA script.
pushd  $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/misc
mv CA.sh CA
popd

mkdir -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA
mkdir -m700 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA/private
mkdir -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA/certs
mkdir -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA/crl
mkdir -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA/newcerts

# Ensure the openssl.cnf timestamp is identical across builds to avoid
# mulitlib conflicts and unnecessary renames on upgrade
touch -r %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/openssl.cnf

# Determine which arch opensslconf.h is going to try to #include.
basearch=%{_arch}
%ifarch %{ix86}
basearch=i386
%endif
%ifarch sparcv9
basearch=sparc
%endif
%ifarch sparc64
basearch=sparc64
%endif

%ifarch %{multilib_arches}
# Do an opensslconf.h switcheroo to avoid file conflicts on systems where you
# can have both a 32- and 64-bit version of the library, and they each need
# their own correct-but-different versions of opensslconf.h to be usable.
install -m644 %{SOURCE10} \
	$RPM_BUILD_ROOT/%{_prefix}/include/openssl/opensslconf-${basearch}.h
cat $RPM_BUILD_ROOT/%{_prefix}/include/openssl/opensslconf.h >> \
	$RPM_BUILD_ROOT/%{_prefix}/include/openssl/opensslconf-${basearch}.h
install -m644 %{SOURCE9} \
	$RPM_BUILD_ROOT/%{_prefix}/include/openssl/opensslconf.h
%endif

# Remove unused files from upstream fips support
#rm -rf $RPM_BUILD_ROOT/%{_bindir}/openssl_fips_fingerprint
#rm -rf $RPM_BUILD_ROOT/%{_libdir}/fips_premain.*
#rm -rf $RPM_BUILD_ROOT/%{_libdir}/fipscanister.*

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc FAQ LICENSE CHANGES NEWS INSTALL README
%doc doc/c-indentation.el doc/openssl.txt
%doc doc/openssl_button.html doc/openssl_button.gif
%doc doc/ssleay.txt
%doc README.FIPS
%{_sysconfdir}/pki/tls/certs/make-dummy-cert
%{_sysconfdir}/pki/tls/certs/Makefile
%{_sysconfdir}/pki/tls/misc/CA
%dir %{_sysconfdir}/pki/CA
%dir %{_sysconfdir}/pki/CA/private
%dir %{_sysconfdir}/pki/CA/certs
%dir %{_sysconfdir}/pki/CA/crl
%dir %{_sysconfdir}/pki/CA/newcerts
%{_sysconfdir}/pki/tls/misc/c_*
%attr(0755,root,root) %{_bindir}/openssl
%attr(0644,root,root) %{_mandir}/man1*/[ABD-Zabcd-z]*
%attr(0644,root,root) %{_mandir}/man5*/*
%attr(0644,root,root) %{_mandir}/man7*/*

%files libs
%defattr(-,root,root)
%doc LICENSE
%dir %{_sysconfdir}/pki/tls
%dir %{_sysconfdir}/pki/tls/certs
%dir %{_sysconfdir}/pki/tls/misc
%dir %{_sysconfdir}/pki/tls/private
%config(noreplace) %{_sysconfdir}/pki/tls/openssl.cnf
%attr(0755,root,root) %{_libdir}/libcrypto.so.%{version}
%attr(0755,root,root) %{_libdir}/libcrypto.so.%{soversion}
%attr(0755,root,root) %{_libdir}/libssl.so.%{version}
%attr(0755,root,root) %{_libdir}/libssl.so.%{soversion}
#%attr(0644,root,root) %{_libdir}/.libcrypto.so.*.hmac
#%attr(0644,root,root) %{_libdir}/.libssl.so.*.hmac
%attr(0755,root,root) %{_libdir}/openssl

%files devel
%defattr(-,root,root)
%{_prefix}/include/openssl
%attr(0755,root,root) %{_libdir}/*.so
%attr(0644,root,root) %{_mandir}/man3*/*
%attr(0644,root,root) %{_libdir}/pkgconfig/*.pc

%files static
%defattr(-,root,root)
%attr(0644,root,root) %{_libdir}/*.a

%files perl
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/c_rehash
%attr(0644,root,root) %{_mandir}/man1*/*.pl*
%{_sysconfdir}/pki/tls/misc/*.pl
%{_sysconfdir}/pki/tls/misc/tsget

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%changelog
* Sat Aug 17 2013 Arnoud Vermeer <a.vermeer@freshway.biz> 1.0.1e-6
- new package built with tito

* Mon Jan 08 2013 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1:1.0.1e-1.ius
- Removing fips patches, now built in.
- Resoves CVE-2013-1069
  http://www.openssl.org/news/secadv_20130205.txt

* Mon Jan 08 2013 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1:1.0.1c-10.ius
- Removing Obsolute

* Tue Dec 04 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1:1.0.1c-9.ius
- Removing Epoch

* Mon Dec 03 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1:1.0.1c-8.ius
- Adding in required Conflicts:
  http://iuscommunity.org/pages/IUSDeveloperGuide.html#ius-packages-provide-conflict-never-obsolete

* Mon Aug 13 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1:1.0.1c-7.ius
- Porting to IUS

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.1c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1c-5
- use __getenv_secure() instead of __libc_enable_secure

* Fri Jul 13 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1c-4
- do not move libcrypto to /lib
- do not use environment variables if __libc_enable_secure is on
- fix strict aliasing problems in modes

* Thu Jul 12 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1c-3
- fix DSA key generation in FIPS mode (#833866)
- allow duplicate FIPS_mode_set(1)
- enable build on ppc64 subarch (#834652)

* Wed Jul 11 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1c-2
- fix s_server with new glibc when no global IPv6 address (#839031)
- make it build with new Perl

* Tue May 15 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1c-1
- new upstream version

* Thu Apr 26 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1b-1
- new upstream version

* Fri Apr 20 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1a-1
- new upstream version fixing CVE-2012-2110

* Wed Apr 11 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1-3
- add Kerberos 5 libraries to pkgconfig for static linking (#807050)

* Thu Apr  5 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1-2
- backports from upstream CVS
- fix segfault when /dev/urandom is not available (#809586)

* Wed Mar 14 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1-1
- new upstream release

* Mon Mar  5 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1-0.3.beta3
- add obsoletes to assist multilib updates (#799636)

* Wed Feb 29 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1-0.2.beta3
- epoch bumped to 1 due to revert to 1.0.0g on Fedora 17
- new upstream release from the 1.0.1 branch
- fix s390x build (#798411)
- versioning for the SSLeay symbol (#794950)
- add -DPURIFY to build flags (#797323)
- filter engine provides
- split the libraries to a separate -libs package
- add make to requires on the base package (#783446)

* Tue Feb  7 2012 Tomas Mraz <tmraz@redhat.com> 1.0.1-0.1.beta2
- new upstream release from the 1.0.1 branch, ABI compatible
- add documentation for the -no_ign_eof option

* Thu Jan 19 2012 Tomas Mraz <tmraz@redhat.com> 1.0.0g-1
- new upstream release fixing CVE-2012-0050 - DoS regression in
  DTLS support introduced by the previous release (#782795)

* Thu Jan  5 2012 Tomas Mraz <tmraz@redhat.com> 1.0.0f-1
- new upstream release fixing multiple CVEs

* Tue Nov 22 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0e-4
- move the libraries needed for static linking to Libs.private

* Thu Nov  3 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0e-3
- do not use AVX instructions when osxsave bit not set
- add direct known answer tests for SHA2 algorithms

* Wed Sep 21 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0e-2
- fix missing initialization of variable in CHIL engine

* Wed Sep  7 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0e-1
- new upstream release fixing CVE-2011-3207 (#736088)

* Wed Aug 24 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0d-8
- drop the separate engine for Intel acceleration improvements
  and merge in the AES-NI, SHA1, and RC4 optimizations
- add support for OPENSSL_DISABLE_AES_NI environment variable
  that disables the AES-NI support

* Tue Jul 26 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0d-7
- correct openssl cms help output (#636266)
- more tolerant starttls detection in XMPP protocol (#608239)

* Wed Jul 20 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0d-6
- add support for newest Intel acceleration improvements backported
  from upstream by Intel in form of a separate engine

* Thu Jun  9 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0d-5
- allow the AES-NI engine in the FIPS mode

* Tue May 24 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0d-4
- add API necessary for CAVS testing of the new DSA parameter generation

* Thu Apr 28 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0d-3
- add support for VIA Padlock on 64bit arch from upstream (#617539)
- do not return bogus values from load_certs (#652286)

* Tue Apr  5 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0d-2
- clarify apps help texts for available digest algorithms (#693858)

* Thu Feb 10 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0d-1
- new upstream release fixing CVE-2011-0014 (OCSP stapling vulnerability)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0c-3
- add -x931 parameter to openssl genrsa command to use the ANSI X9.31
  key generation method
- use FIPS-186-3 method for DSA parameter generation
- add OPENSSL_FIPS_NON_APPROVED_MD5_ALLOW environment variable
  to allow using MD5 when the system is in the maintenance state
  even if the /proc fips flag is on
- make openssl pkcs12 command work by default in the FIPS mode

* Mon Jan 24 2011 Tomas Mraz <tmraz@redhat.com> 1.0.0c-2
- listen on ipv6 wildcard in s_server so we accept connections
  from both ipv4 and ipv6 (#601612)
- fix openssl speed command so it can be used in the FIPS mode
  with FIPS allowed ciphers

* Fri Dec  3 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0c-1
- new upstream version fixing CVE-2010-4180

* Tue Nov 23 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0b-3
- replace the revert for the s390x bignum asm routines with
  fix from upstream

* Mon Nov 22 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0b-2
- revert upstream change in s390x bignum asm routines

* Tue Nov 16 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0b-1
- new upstream version fixing CVE-2010-3864 (#649304)

* Tue Sep  7 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0a-3
- make SHLIB_VERSION reflect the library suffix

* Wed Jun 30 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0a-2
- openssl man page fix (#609484)

* Fri Jun  4 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0a-1
- new upstream patch release, fixes CVE-2010-0742 (#598738)
  and CVE-2010-1633 (#598732)

* Wed May 19 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-5
- pkgconfig files now contain the correct libdir (#593723)

* Tue May 18 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-4
- make CA dir readable - the private keys are in private subdir (#584810)

* Fri Apr  9 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-3
- a few fixes from upstream CVS
- move libcrypto to /lib (#559953)

* Tue Apr  6 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-2
- set UTC timezone on pod2man run (#578842)
- make X509_NAME_hash_old work in FIPS mode

* Tue Mar 30 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-1
- update to final 1.0.0 upstream release

* Tue Feb 16 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.22.beta5
- make TLS work in the FIPS mode

* Fri Feb 12 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.21.beta5
- gracefully handle zero length in assembler implementations of
  OPENSSL_cleanse (#564029)
- do not fail in s_server if client hostname not resolvable (#561260)

* Wed Jan 20 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.20.beta5
- new upstream release

* Thu Jan 14 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.19.beta4
- fix CVE-2009-4355 - leak in applications incorrectly calling
  CRYPTO_free_all_ex_data() before application exit (#546707)
- upstream fix for future TLS protocol version handling

* Wed Jan 13 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.18.beta4
- add support for Intel AES-NI

* Thu Jan  7 2010 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.17.beta4
- upstream fix compression handling on session resumption
- various null checks and other small fixes from upstream
- upstream changes for the renegotiation info according to the latest draft

* Mon Nov 23 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.16.beta4
- fix non-fips mingw build (patch by Kalev Lember)
- add IPV6 fix for DTLS

* Fri Nov 20 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.15.beta4
- add better error reporting for the unsafe renegotiation

* Fri Nov 20 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.14.beta4
- fix build on s390x

* Wed Nov 18 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.13.beta4
- disable enforcement of the renegotiation extension on the client (#537962)
- add fixes from the current upstream snapshot

* Fri Nov 13 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.12.beta4
- keep the beta status in version number at 3 so we do not have to rebuild
  openssh and possibly other dependencies with too strict version check

* Thu Nov 12 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.11.beta4
- update to new upstream version, no soname bump needed
- fix CVE-2009-3555 - note that the fix is bypassed if SSL_OP_ALL is used
  so the compatibility with unfixed clients is not broken. The
  protocol extension is also not final.

* Fri Oct 16 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.10.beta3
- fix use of freed memory if SSL_CTX_free() is called before
  SSL_free() (#521342)

* Thu Oct  8 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.9.beta3
- fix typo in DTLS1 code (#527015)
- fix leak in error handling of d2i_SSL_SESSION()

* Wed Sep 30 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.8.beta3
- fix RSA and DSA FIPS selftests
- reenable fixed x86_64 camellia assembler code (#521127)

* Fri Sep  4 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.7.beta3
- temporarily disable x86_64 camellia assembler code (#521127)

* Mon Aug 31 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.6.beta3
- fix openssl dgst -dss1 (#520152)

* Wed Aug 26 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.5.beta3
- drop the compat symlink hacks

* Sat Aug 22 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.4.beta3
- constify SSL_CIPHER_description()

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.3.beta3
- fix WWW:Curl:Easy reference in tsget

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.2.beta3
- enable MD-2

* Thu Aug 20 2009 Tomas Mraz <tmraz@redhat.com> 1.0.0-0.1.beta3
- update to new major upstream release
