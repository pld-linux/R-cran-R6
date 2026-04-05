%define		fversion	%(echo %{version} |tr r -)
%define		modulename	R6
%undefine	_debugsource_packages
Summary:	Encapsulated classes with reference semantics
Name:		R-cran-%{modulename}
Version:	2.6.1
Release:	3
License:	MIT
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	f01b1787f12797c29194d63c9afd5d70
URL:		https://cran.r-project.org/package=%{modulename}
BuildRequires:	R
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Encapsulated classes with reference semantics.

%prep
%setup -q -c

%build
R CMD build --no-build-vignettes %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
