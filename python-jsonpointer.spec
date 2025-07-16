#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-jsonpointer.spec)

Summary:	Identify specific nodes in a JSON document (RFC 6901)
Summary(pl.UTF-8):	Identyfikowanie określonych węzłów w dokumencie JSON (RFC 6901)
Name:		python-jsonpointer
# keep 2.x here for python2 support
Version:	2.4
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jsonpointer/
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
# Source0-md5:	16d785130e5ff235e4ae336eaa611e13
URL:		https://pypi.org/project/jsonpointer/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library and tool to resolve JSON Pointers according to RFC 6901.

%description -l pl.UTF-8
Biblioteka i narzędzie do rozwiązywania wskaźników JSON zgodnie z RFC
6901.

%package -n python3-jsonpointer
Summary:	Identify specific nodes in a JSON document (RFC 6901)
Summary(pl.UTF-8):	Identyfikowanie określonych węzłów w dokumencie JSON (RFC 6901)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.7
Obsoletes:	jsonpointer < 2.4

%description -n python3-jsonpointer
Library and tool to resolve JSON Pointers according to RFC 6901.

%description -n python3-jsonpointer -l pl.UTF-8
Biblioteka i narzędzie do rozwiązywania wskaźników JSON zgodnie z RFC
6901.

%prep
%setup -q -n jsonpointer-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/jsonpointer{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/jsonpointer{,-3}
ln -sf jsonpointer-3 $RPM_BUILD_ROOT%{_bindir}/jsonpointer
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE.txt README.md
%attr(755,root,root) %{_bindir}/jsonpointer-2
%{py_sitescriptdir}/jsonpointer.py[co]
%{py_sitescriptdir}/jsonpointer-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-jsonpointer
%defattr(644,root,root,755)
%doc AUTHORS LICENSE.txt README.md
%attr(755,root,root) %{_bindir}/jsonpointer
%attr(755,root,root) %{_bindir}/jsonpointer-3
%{py3_sitescriptdir}/jsonpointer.py
%{py3_sitescriptdir}/__pycache__/jsonpointer.cpython-*.py[co]
%{py3_sitescriptdir}/jsonpointer-%{version}-py*.egg-info
%endif
