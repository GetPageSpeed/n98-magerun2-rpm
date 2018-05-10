# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun2
Version: 2.1.2
Release: 2%{?dist}
Summary: n98-magerun2. The swiss army knife for Magento developers

License: GPLv2+ and MIT and BSD
URL: https://magerun.net/
Source0: https://files.magerun.net/n98-magerun2-%{version}.phar

BuildArch: noarch

Requires:  php(language) >= 5.5
Requires:  php-mbstring
Requires:  php-openssl
Requires:  php-xml

# TODO: Get info from phpcompatinfo reports for 2.1.2


%description
The swiss army knife for Magento developers, sysadmins and devops.
The tool provides a huge set of well tested command line commands which save hours
of work time. All commands are extendable by a module API.


%prep
# Nothing to do


%build
# Nothing to do


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -p %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/magerun2

%files
%defattr(-,root,root)
%{_bindir}/magerun2


%changelog
* Sun Mar 4 2018 Danila Vershinin <info@getpagespeed.com> 2.1.2-1
- update to 2.1.2

