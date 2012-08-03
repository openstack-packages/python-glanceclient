Name:             python-glanceclient
Version:          2012.2
Release:          0.3.f1%{?dist}
Summary:          Python API and CLI for OpenStack Glance

Group:            Development/Languages
License:          ASL 2.0
URL:              http://github.com/openstack/python-glanceclient
Source0:          http://launchpad.net/glance/folsom/folsom-1/+download/python-glanceclient-2012.2~f1.tar.gz

Patch0:           glanceclient-remove-argparse-from-egg-requires.patch

BuildArch:        noarch
BuildRequires:    python-setuptools

Requires:         python-argparse
Requires:         python-httplib2
Requires:         python-prettytable
Requires:         python-keystoneclient

Conflicts:        openstack-glance < 2012.2

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# rename client script to avoid conflict with old glance client
# from openstack-glance RPM
mv %{buildroot}%{_bindir}/glance %{buildroot}%{_bindir}/glance-client

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/tests

%files
%doc README.rst
%doc LICENSE
%{_bindir}/glance-client
%{python_sitelib}/glanceclient
%{python_sitelib}/*.egg-info

%changelog
* Fri Aug 03 2012 Alan Pevec <apevec@redhat.com> 2012.2-0.3.f1
- rename client script to avoid conflict with old glance client

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.2-0.2.f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Pádraig Brady <P@draigBrady.com> 2012.2-0.1.f1
- Initial (folsom-1) release
