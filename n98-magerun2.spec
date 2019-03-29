# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun2
Version: 3.0.6
Release: 1%{?dist}
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
%{__install} -m 755 -p %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%changelog
* Fri Mar 29 2019 Danila Vershinin <info@getpagespeed.com> 3.0.6-1
- upstream version auto-updated to 3.0.6

* Wed Mar 27 2019 Danila Vershinin <info@getpagespeed.com> 3.0.5-1
- upstream version auto-updated to 3.0.5

* Tue Feb 05 2019 Danila Vershinin <info@getpagespeed.com> 3.0.4-1
- upstream version auto-updated to 3.0.4

* Fri Dec 21 2018 Danila Vershinin <info@getpagespeed.com> 3.0.3-1
- upstream version auto-updated to 3.0.3

* Fri Dec 14 2018 Danila Vershinin <info@getpagespeed.com> 3.0.2-1
- upstream version auto-updated to 3.0.2

* Mon Dec 10 2018 Danila Vershinin <info@getpagespeed.com> 3.0.1-1
- upstream version auto-updated to 3.0.1

* Sat Dec 08 2018 Danila Vershinin <info@getpagespeed.com> 3.0.0-1
- upstream version auto-updated to 3.0.0

* Sun Nov 18 2018 Danila Vershinin <info@getpagespeed.com> 2.3.3-1
- upstream version auto-updated to 2.3.3

* Thu Nov 08 2018 Danila Vershinin <info@getpagespeed.com> 2.3.2-1
- upstream version auto-updated to 2.3.2

* Fri Oct 19 2018 Danila Vershinin <info@getpagespeed.com> 2.3.1-1
- upstream version auto-updated to 2.3.1

* Sun Oct 14 2018 Danila Vershinin <info@getpagespeed.com> 2.3.0-1
- upstream version auto-updated to 2.3.0

* Sat Oct 13 2018 Danila Vershinin <info@getpagespeed.com> 2.2.0-1
- upstream version auto-updated to 2.2.0

* Sun Mar 4 2018 Danila Vershinin <info@getpagespeed.com> 2.1.2-1
- update to 2.1.2

