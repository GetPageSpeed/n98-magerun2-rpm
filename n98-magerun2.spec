%global upstream_github netz98
# %%global upstream_prefix v
%global upstream_prefix %{nil}

# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun2
Version: 4.0.2
Release: 1%{?dist}.gps
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
Summary:        A bash completion helper for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       bash-completion

%description completion-bash
Install this package to enable tab-completion of functions and installed
modules with the %{name} command in bash shell.


%package completion-zsh
Group:          System Environment/Shells
Summary:        A zsh completion helper for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       zsh

%description completion-zsh
Install this package to enable tab-completion of functions and installed
modules with the %{name} command in zsh shell.


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
%if 0%{?rhel} && 0%{?rhel} < 7
%{__install} -Dp -m0644 res/autocompletion/bash/%{name}.phar.bash \
  $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}.bash
%else
%{__install} -Dp -m0644 res/autocompletion/bash/%{name}.phar.bash \
  $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/%{name}
%endif

# zsh completions
%if 0%{?rhel} && 0%{?rhel} <= 8
%{__install} -Dp -m0644 res/autocompletion/zsh/%{name}.plugin.zsh \
  $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_%{name}
%else
%{__install} -Dp -m0644 res/autocompletion/zsh/%{name}.plugin.zsh \
  $RPM_BUILD_ROOT%{_datadir}/zsh/vendor-completions/_%{name}
%endif


%post completion-bash
. /etc/profile.d/bash_completion.sh


%postun completion-bash
. /etc/profile.d/bash_completion.sh


%files
%defattr(-,root,root)
%{_bindir}/%{name}
# Virtually add license macro for EL6:
%{!?_licensedir:%global license %%doc}
%license MIT-LICENSE.txt
%doc README.md SECURITY.md CHANGELOG.md

%files completion-bash
%if 0%{?rhel} && 0%{?rhel} < 7
%config %{_sysconfdir}/bash_completion.d/*
%else
%{_datadir}/bash-completion/completions/%{name}
%endif


%files completion-zsh
%if 0%{?rhel} && 0%{?rhel} <= 8
%{_datadir}/zsh/site-functions/_%{name}
%else
%{_datadir}/zsh/vendor-completions/_%{name}
%endif


%changelog
* Wed Feb 19 2020 Danila Vershinin <info@getpagespeed.com> 4.0.3.4.0.3-1
- upstream version auto-updated to 4.0.3.4.0.3

* Wed Jan 22 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Wed Jan 22 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Tue Jan 21 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Mon Jan 20 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Sun Jan 19 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Sat Jan 18 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Fri Jan 17 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Thu Jan 16 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Tue Jan 14 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Mon Jan 13 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Sat Jan 11 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Fri Jan 10 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Thu Jan 09 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2.4.0.2-1
- upstream version auto-updated to 4.0.2.4.0.2

* Fri Jan 03 2020 Danila Vershinin <info@getpagespeed.com> 4.0.2-1
- new upstream release
- added zsh completions subpackage
- install bash completions into "faster" location depending on distro
- fixed arch dependency from bash completions

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

