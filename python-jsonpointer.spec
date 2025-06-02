#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

Summary:	Identify specific nodes in a JSON document (RFC 6901)
Summary(pl.UTF-8):	Identyfikowanie określonych węzłów w dokumencie JSON (RFC 6901)
Name:		python-jsonpointer
Version:	2.3
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jsonpointer/
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
# Source0-md5:	57fd6581e61d56960d8c2027ff33f5c0
URL:		https://pypi.org/project/jsonpointer/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to resolve JSON Pointers according to RFC 6901.

%description -l pl.UTF-8
Biblioteka do rozwiązywania wskaźników JSON zgodnie z RFC 6901.

%package -n python3-jsonpointer
Summary:	Identify specific nodes in a JSON document (RFC 6901)
Summary(pl.UTF-8):	Identyfikowanie określonych węzłów w dokumencie JSON (RFC 6901)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-jsonpointer
Library to resolve JSON Pointers according to RFC 6901.

%description -n python3-jsonpointer -l pl.UTF-8
Biblioteka do rozwiązywania wskaźników JSON zgodnie z RFC 6901.

%package -n jsonpointer
Summary:	Identify specific nodes in a JSON document (RFC 6901)
Summary(pl.UTF-8):	Identyfikowanie określonych węzłów w dokumencie JSON (RFC 6901)
Group:		Applications/Text
%if %{with python3}
Requires:	python3-jsonpointer = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n jsonpointer
Tool to resolve JSON Pointers according to RFC 6901.

%description -n jsonpointer -l pl.UTF-8
Narzędzie do rozwiązywania wskaźników JSON zgodnie z RFC 6901.

%prep
%setup -q -n jsonpointer-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
# install may not overwrite existing file
%{__rm} -f $RPM_BUILD_ROOT%{_bindir}/jsonpointer
%py3_install
%else
%{__mv} $RPM_BUILD_ROOT%{_bindir}/jsonpointer{,-2}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE.txt README.md
%{py_sitescriptdir}/jsonpointer.py[co]
%{py_sitescriptdir}/jsonpointer-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-jsonpointer
%defattr(644,root,root,755)
%doc AUTHORS LICENSE.txt README.md
%{py3_sitescriptdir}/jsonpointer.py
%{py3_sitescriptdir}/__pycache__/jsonpointer.cpython-*.py[co]
%{py3_sitescriptdir}/jsonpointer-%{version}-py*.egg-info
%endif

%files -n jsonpointer
%defattr(644,root,root,755)
%if %{with python3}
%attr(755,root,root) %{_bindir}/jsonpointer
%endif
%attr(755,root,root) %{_bindir}/jsonpointer-2
