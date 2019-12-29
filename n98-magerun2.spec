%global upstream_github netz98
# %%global upstream_prefix v
%global upstream_prefix %{nil}

# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun2
Version: 3.2.0
Release: 2%{?dist}
Summary: The Swiss Army knife for Magento 2 developers

License: GPLv2+ and MIT and BSD
URL: https://github.com/%{upstream_github}/%{name}
Source0: %{url}/archive/%{upstream_prefix}%{version}/%{name}-%{upstream_prefix}%{version}.tar.gz
Source100: https://files.magerun.net/n98-magerun2-%{version}.phar

BuildArch: noarch

Requires:  php(language) >= 5.5
Requires:  php-mbstring
Requires:  php-openssl
Requires:  php-xml

# TODO: Get info from phpcompatinfo reports for 2.1.2
# TODO actually build this stuff

%description
The swiss army knife for Magento developers, sysadmins and devops.
The tool provides a huge set of well tested command line commands
which save hours of work time.

All commands are extendable by a module API.


%package completion-bash
Group:          System Environment/Shells
Summary:        A bash completion helper for n98-magerun2
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       bash-completion


%description completion-bash
Install this package to enable tab-completion of functions and installed
modules with the magerun2 command.


%prep
%autosetup -n %{name}-%{version}
# remove shebang from bash completions
sed -i -e '1d' res/autocompletion/bash/%{name}.phar.bash


%build
# Nothing to do


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -p %SOURCE100 $RPM_BUILD_ROOT%{_bindir}/%{name}
# bash completions
%{__install} -d -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
%{__install} -Dp -m0644 res/autocompletion/bash/%{name}.phar.bash \
  $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}.bash


%post
. /etc/profile.d/bash_completion.sh


%postun
. /etc/profile.d/bash_completion.sh


%files
%defattr(-,root,root)
%{_bindir}/%{name}


%files completion-bash
%config %{_sysconfdir}/bash_completion.d/*


%changelog
* Sun Dec 29 2019 Danila Vershinin <info@getpagespeed.com> 3.2.0-2
- one spec uniting bash completions package as well
- proper permissions to bash completions
- remove shebang from bash completions

* Sat Jul 20 2019 Danila Vershinin <info@getpagespeed.com> 3.2.0-1
- upstream version auto-updated to 3.2.0

* Sun Jun 30 2019 Danila Vershinin <info@getpagespeed.com> 3.1.0-1
- upstream version auto-updated to 3.1.0

* Tue Jun 11 2019 Danila Vershinin <info@getpagespeed.com> 3.0.10-1
- upstream version auto-updated to 3.0.10

* Sat Jun 01 2019 Danila Vershinin <info@getpagespeed.com> 3.0.9-1
- upstream version auto-updated to 3.0.9

* Thu Apr 11 2019 Danila Vershinin <info@getpagespeed.com> 3.0.8-1
- upstream version auto-updated to 3.0.8

* Tue Apr 02 2019 Danila Vershinin <info@getpagespeed.com> 3.0.7-1
- upstream version auto-updated to 3.0.7

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

