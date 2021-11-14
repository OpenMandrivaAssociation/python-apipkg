# Created by pyp2rpm-2.0.0
%global pypi_name apipkg
#%%define tarname setuptools-scm
%global with_python2 1
%define version 1.5

Name:           python-%{pypi_name}
Version:	2.1.0
Release:	1
Group:          Development/Python
Summary:        Control the exported namespace of a Python package

License:        MIT
Url:            https://github.com/pytest-dev/apipkg
# See also      https://github.com/pypa/setuptools_scm
Source0:	https://files.pythonhosted.org/packages/46/90/c54454c5f87ae7c754626cdc71499f6c1b3d7cdd13a4a7f27a20e05a1ad3/apipkg-2.1.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python-setuptools_scm
 
%if %{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
%endif # if with_python2


%description
With apipkg you can control the exported namespace of a Python package and greatly reduce the number of imports for your users. It is a small pure Python module that works on CPython 2.7 and 3.4+, Jython and PyPy. It cooperates well with Python’s help() system, custom importers (PEP302) and common command-line completion tools.

%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        Control the exported namespace of a Python package 

%description -n python2-%{pypi_name}
With apipkg you can control the exported namespace of a Python package and greatly reduce the number of imports for your users. It is a small pure Python module that works on CPython 2.7 and 3.4+, Jython and PyPy. It cooperates well with Python’s help() system, custom importers (PEP302) and common command-line completion tools.

%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif # with_python2


%build
%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2


%install

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc  README.rst LICENSE
%{python_sitelib}/*/*
#%%{python_sitelib}/pep8.py


%if %{with_python2}
%files -n python2-%{pypi_name}
%doc  README.rst LICENSE
%{python2_sitelib}/*/*
#%%{python2_sitelib}/pep8.*
%endif # with_python2

