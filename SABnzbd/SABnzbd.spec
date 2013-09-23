# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		SABnzbd
Version:	0.7.11
Release:	1.1
License:	GPL-2.0
Summary:	An open source binary newsreader written in Python
Url:		http://sabnzbd.org
Group:		Productivity/Networking/News/Clients

Source:		http://downloads.sourceforge.net/project/sabnzbdplus/sabnzbdplus/%{version}/SABnzbd-%{version}-src.tar.gz
Source1:	SABnzbd.desktop
Source2:	SABnzbd.service
Source3:	SABnzbd.sysconfig

BuildRequires:	fdupes
BuildRequires:	python
BuildRequires:	systemd
BuildRequires:	update-desktop-files

Requires:	par2cmdline
Requires:	python-Cheetah
Requires:	python-pyOpenSSL
Requires:	python-yenc
Requires:	unrar
Requires:	unzip
%{systemd_requires}

PreReq:		%fillup_prereq

BuildArch:	noarch

%description
SABnzbd makes Usenet as simple and streamlined as possible by automating
everything we can. All you have to do is add an .nzb. SABnzbd takes over from
there, where it will be automatically downloaded, verified, repaired, extracted
and filed away with zero human interaction.


%prep
%setup -q


%build
# Create translation files
python tools/make_mo.py


%install
install -dm755 $RPM_BUILD_ROOT%{_datadir}/SABnzbd/

find . -maxdepth 1 -type d \
  ! -name po -a \
  ! -name locale -a \
  ! -name licenses -a \
  ! -name . \
  -print > dirs

while read LINE; do
  find ${LINE} -type f \
    -exec install -Dm644 {} $RPM_BUILD_ROOT%{_datadir}/SABnzbd/{} \;
done < dirs

rm dirs

install -m755 ./SABnzbd.py $RPM_BUILD_ROOT%{_datadir}/SABnzbd/

# Install translations
find locale -type f -exec \
  install -Dm644 {} $RPM_BUILD_ROOT%{_datadir}/SABnzbd/{} \;
%find_lang SABnzbd

# Install desktop file
install -dm755 $RPM_BUILD_ROOT%{_datadir}/applications/
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/
%suse_update_desktop_file %{name}

# Install systemd service
install -dm755 $RPM_BUILD_ROOT%{_unitdir}/
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/

# Install sysconfig file
install -dm755 $RPM_BUILD_ROOT%{_localstatedir}/adm/fillup-templates/
install -m644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_localstatedir}/adm/fillup-templates/sysconfig.%{name}

# Remove shebang lines from the Python 2 files to avoid rpmlint's
# non-executable-script error.
find $RPM_BUILD_ROOT -type f -name '*.py' -a ! -name 'SABnzbd.py' -exec \
  sed -i '/^#!/d' {} \;

# Cherry daemon should be executable
chmod 755 $RPM_BUILD_ROOT%{_datadir}/SABnzbd/cherrypy/cherryd

# Link duplicate files together to save space
%fdupes $RPM_BUILD_ROOT

# Remove duplicate GPL-2.0 and GPL-3.0 license files
rm -v \
  $RPM_BUILD_ROOT%{_datadir}/SABnzbd/interfaces/Plush/licenses/LICENSE-GPL3.txt
rm -v $RPM_BUILD_ROOT%{_datadir}/SABnzbd/interfaces/smpl/GPL2.txt
rm -v $RPM_BUILD_ROOT%{_datadir}/SABnzbd/interfaces/smpl/GPL3.txt

# Remove empty files
find $RPM_BUILD_ROOT -type f -empty -delete


%pre
%service_add_pre SABnzbd.service

%post
%service_add_post SABnzbd.service
%{fillup_only SABnzbd}

%preun
%service_del_preun SABnzbd.service

%postun
%service_del_postun SABnzbd.service


%files -f SABnzbd.lang
%defattr(-,root,root)
%doc CHANGELOG.txt COPYRIGHT.txt GPL2.txt GPL3.txt ISSUES.txt README.txt
%doc licenses/
%{_unitdir}/SABnzbd.service
%{_datadir}/applications/SABnzbd.desktop
%{_datadir}/SABnzbd/
%{_localstatedir}/adm/fillup-templates/sysconfig.%{name}


%changelog
* Mon Mar 18 2013 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.7.11-1
- Version 0.7.11

* Wed Aug 15 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.7.3-2
- Put locales in /usr/share/SABnzbd

* Wed Aug 15 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.7.3-1
- Initial release
- Version 0.7.3
