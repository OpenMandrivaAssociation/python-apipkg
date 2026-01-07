%global module apipkg
%bcond tests 1

Name:		python-apipkg
Version:	3.0.2
Release:	1
Group:		Development/Python
Summary:	Control the exported namespace of a Python package
License:	MIT
URL:		https://github.com/pytest-dev/apipkg
Source0:	https://github.com/pytest-dev/apipkg/archive/v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# See for patch info: https://github.com/pytest-dev/apipkg/pull/58
Patch0:		support-pytest9.patch

BuildSystem:	python
BuildArch:		noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
With apipkg you can control the exported namespace of a Python package and greatly reduce the number of imports for your users. It is a small pure Python module that works on CPython 2.7 and 3.4+, Jython and PyPy. It cooperates well with Python’s help() system, custom importers (PEP302) and common command-line completion tools.

%prep
%autosetup -n %{module}-%{version} -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%py_build

%install
%py_install

%if %{with tests}
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -v
#-k 'not test_get_distribution_version'
%endif

%files
%doc  README.rst
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
