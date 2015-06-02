Name:             python-glanceclient
Epoch:            1
Version:          XXX
Release:          XXX{?dist}
Summary:          Python API and CLI for OpenStack Glance

Group:            Development/Languages
License:          ASL 2.0
URL:              http://github.com/openstack/python-glanceclient
Source0:          https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    python2-devel
BuildRequires:    python-setuptools
BuildRequires:    python-d2to1
BuildRequires:    python-pbr
BuildRequires:    python-sphinx
BuildRequires:    python-oslo-sphinx

Requires:         python-httplib2
Requires:         python-keystoneclient
Requires:         python-oslo-utils
Requires:         python-pbr
Requires:         python-prettytable
Requires:         python-requests
Requires:         python-setuptools
Requires:         python-warlock
Requires:         pyOpenSSL

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.


%package doc
Summary:          Documentation for OpenStack Nova API Client
Group:            Documentation

BuildRequires:    python-sphinx

%description      doc
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.

This package contains auto-generated documentation.


%prep
%setup -q -n %{name}-%{upstream_version}

# Remove bundled egg-info
rm -rf python_glanceclient.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# generate man page
sphinx-build -b man doc/source man
install -p -D -m 644 man/glance.1 %{buildroot}%{_mandir}/man1/glance.1


%files
%doc README.rst
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/glance
%{python2_sitelib}/glanceclient
%{python2_sitelib}/*.egg-info
%{_mandir}/man1/glance.1.gz

%files doc
%doc html


%changelog
