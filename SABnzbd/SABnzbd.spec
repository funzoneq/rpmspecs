#global sabrc             RC2

Name:			SABnzbd
Version:		0.7.16
Release:		1%{?dist}
Summary:		An Open Source Binary Newsreader written in Python
Group:			Applications/Internet
License:		GPLv2
URL:			http://sabnzbd.org/

#Source0:		SABnzbd-%{version}%{?sabrc}-src.tar.gz
Source0:                http://downloads.sourceforge.net/project/sabnzbdplus/sabnzbdplus/%{version}/SABnzbd-%{version}-src.tar.gz
Source1:		SABnzbd.sh
Source2:		SABnzbd.desktop
Source3:		SABnzbd.initd
Source4:		SABnzbd.sysconfig

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:		noarch

BuildRequires:		desktop-file-utils
%if 0%{?rhel} == 5
BuildRequires:		python26-devel
BuildRequires:		python26-setuptools
%global pyver 26
%global pybasever 2.6

%global __python /usr/bin/python%{pybasever}
%global __os_install_post %{__python26_os_install_post}
%else
BuildRequires:		python-devel
BuildRequires:		python-setuptools
%endif

Requires:		nc
Requires:		par2cmdline
%if 0%{?rhel} == 5
Requires:		python26
Requires:		pyOpenSSL26
Requires:		python26-cheetah
Requires:		python26-yenc
%else
Requires:		pyOpenSSL
Requires:		python-cheetah
Requires:		python-yenc
%endif
Requires:		unrar
Requires:		unzip
Requires:		wget

Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(postun):	initscripts

Obsoletes:		SABnzbd-beta

%description
SABnzbd makes Usenet as simple and streamlined as possible by automating
everything it can. All you have to do is add an .nzb. SABnzbd takes over
from there, where it will be automatically downloaded, verified, repaired,
extracted and filed away with zero human interaction.

%prep
%setup -q -n SABnzbd-%{version}%{?sabrc}

%build

%if 0%{?rhel} == 5
sed -i "s|/usr/bin/python|/usr/bin/python26|g" %{_builddir}/SABnzbd-%{version}%{?sabrc}/SABnzbd.py
%endif
sed -i "s|@DATADIR@|%{_datadir}|g" %{SOURCE1} %{SOURCE2} %{SOURCE3}

%install

rm -rf %{buildroot}

#SABnzbd
%{__install} -d -m0755  %{buildroot}%{_datadir}/SABnzbd
for dir in email interfaces locale po util tools sabnzbd cherrypy SABnzbd.py* icons gntp;do
%{__cp} -a %{_builddir}/SABnzbd-%{version}%{?sabrc}/$dir %{buildroot}%{_datadir}/SABnzbd
done

#start script
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -D -m0755 %{SOURCE1} %{buildroot}%{_bindir}/SABnzbd

#desktop file
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor fedora --dir %{buildroot}%{_datadir}/applications %{SOURCE2}

#init script
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/init.d
%{__install} -D -m0755 %{SOURCE3} %{buildroot}%{_sysconfdir}/init.d/SABnzbd
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -D -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/SABnzbd


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.txt COPYRIGHT.txt GPL2.txt GPL3.txt INSTALL.txt ISSUES.txt README.txt Sample-PostProc.sh licenses/*
%{_bindir}/SABnzbd
%{_datadir}/SABnzbd
%{_datadir}/applications/fedora-SABnzbd.desktop
%{_sysconfdir}/init.d/SABnzbd
%config(noreplace) %{_sysconfdir}/sysconfig/SABnzbd

%post
update-desktop-database &>/dev/null ||:
/sbin/chkconfig --add SABnzbd

%preun
if [ $1 = 0 ] ; then
    /sbin/service SABnzbd stop >/dev/null 2>&1
    /sbin/chkconfig --del SABnzbd
fi

%postun
if [ "$1" -ge "1" ] ; then
    /sbin/service SABnzbd condrestart >/dev/null 2>&1 || :
fi
update-desktop-database &> /dev/null ||:


%changelog