Name:           freshway-release
Version:        1
Release:        0
Summary:        FreshWay Packages for Enterprise Linux repository configuration

Group:          System Environment/Base
License:        GPLv2

# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
URL:            http://vps.us.freshway.biz/CentOS-6-Production-x86_64/RPMS.freshway/
Source0:        GPL
Source1:        freshway.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release >=  %{version}
Conflicts:     fedora-release

%description
This package contains the FreshWay Packages for Enterprise Linux (FPEL) repository
configuration for yum and up2date.

%prep
%setup -q  -c -T

%build


%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun


%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*


%changelog
