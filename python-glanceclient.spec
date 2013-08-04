Name:             python-glanceclient
Epoch:            1
Version:          0.9.0
Release:          3%{?dist}
Summary:          Python API and CLI for OpenStack Glance

Group:            Development/Languages
License:          ASL 2.0
URL:              http://github.com/openstack/python-glanceclient
Source0:          https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

#
# patches_base=0.9.0
#
Patch0001: 0001-Fix-problem-running-glance-version.patch
Patch0002: 0002-Fix-glance-add-parsing-of-copy_from-option.patch
Patch0003: 0003-bug-1166263-image-update-handling-for-closed-stdin.patch

BuildArch:        noarch
BuildRequires:    python-setuptools

Requires:         python-httplib2
Requires:         python-keystoneclient >= 1:0.1.2
Requires:         python-prettytable
Requires:         python-setuptools
Requires:         python-warlock
Requires:         pyOpenSSL

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.

%prep
%setup -q

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1

# Remove bundled egg-info
rm -rf python_glanceclient.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# generate versioninfo
echo "%{version}" > %{buildroot}%{python_sitelib}/glanceclient/versioninfo

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/tests

%files
%doc README.rst
%doc LICENSE
%{_bindir}/glance
%{python_sitelib}/glanceclient
%{python_sitelib}/*.egg-info

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 Jakub Ruzicka <jruzicka@redhat.com> - 1:0.9.0-2
- versioninfo is gone from tarball, generate it.

* Mon May 06 2013 Jakub Ruzicka <jruzicka@redhat.com> - 1:0.9.0-1
- Update to 0.9.0.
- Include selected fixes.

* Wed Mar 27 2013 Pádraig Brady <P@draigBrady.com> - 1:0.8.0-2
- Add a dependency on pyOpenSSL

* Mon Mar 11 2013 Jakub Ruzicka <jruzicka@redhat.com> - 1:0.8.0-1
- Update to 0.8.0.
- Switch from tarballs.openstack.org to pypi sources.

* Wed Jan 30 2013 Alan Pevec <apevec@redhat.com> 1:0.7.0-1
- Update to 0.7.0

* Fri Nov 23 2012 Alan Pevec <apevec@redhat.com> 1:0.6.0-1
- Update to 0.6.0

* Sat Sep 15 2012 Alan Pevec <apevec@redhat.com> 1:0.5.1-1
- Update to 0.5.1

* Wed Aug 22 2012 Alan Pevec <apevec@redhat.com> 1:0.4.1-1
- Add dependency on python-setuptools (#850844)
- Revert client script rename, old glance client is now deprecated.
- New upstream release.

* Fri Aug 03 2012 Alan Pevec <apevec@redhat.com> 2012.2-0.3.f1
- rename client script to avoid conflict with old glance client

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.2-0.2.f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Pádraig Brady <P@draigBrady.com> 2012.2-0.1.f1
- Initial (folsom-1) release