%global upstream_github netz98
# %%global upstream_prefix v
%global upstream_prefix %{nil}

%global box_phar %{SOURCE1}

# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun2
Version: 9.0.2
Release: 1%{?dist}
Summary: The Swiss Army knife for Magento 2 developers

License: GPLv2+ and MIT and BSD
URL: https://github.com/%{upstream_github}/%{name}
Source0: %{url}/archive/%{upstream_prefix}%{version}.tar.gz
Source1: https://github.com/box-project/box/releases/download/3.14.0/box.phar

BuildArch: noarch

BuildRequires: php-cli
BuildRequires: composer
BuildRequires: php-xml
BuildRequires: php-pdo
BuildRequires: php-json
# provides required ext-iconv, ext-posix, ext-zip
BuildRequires: php-common

Requires:  php(language) >= 7.4
Requires:  php-mbstring
Requires:  php-openssl
Requires:  php-xml
Requires:  php-pdo
Requires:  php-json
Requires:  php-common


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
# -S git will init a git repo, required for building phar
%autosetup -n %{name}-%{version} -S git

# remove shebang from bash completions
sed -i -e '1d' res/autocompletion/bash/%{name}.phar.bash

chmod 0755 %{SOURCE1}


%build
ulimit -Sn "$(ulimit -Hn)"
PHP_COMMAND="%{_bindir}/php -d phar.readonly=0"
COMPOSER_CMD="${PHP_COMMAND} %{_bindir}/composer"

# allow composer to run as root
export COMPOSER_ALLOW_SUPERUSER=1

# set composer suffix, otherwise Composer will generate a file with a unique identifier
# which will then create a no reproducable phar file with a differenz MD5
$COMPOSER_CMD config autoloader-suffix N98MagerunNTS

$COMPOSER_CMD install
$PHP_COMMAND %{box_phar} compile

# unset composer suffix
$COMPOSER_CMD config autoloader-suffix --unset

# Set timestamp of newly generted phar file to the commit timestamp
# $PHP_BIN -f build/phar/phar-timestamp.php -- $LAST_COMMIT_TIMESTAMP

# Run a signature verification after the timestamp manipulation
$PHP_COMMAND %{box_phar} verify %{name}.phar

# make phar executable
chmod +x %{name}.phar

# Print version of new phar file which is also a test
$PHP_COMMAND -f %{name}.phar -- --version

# List new phar file for debugging
ls -al "%{name}.phar"


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -p %{name}.phar $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s ./%{name} %{buildroot}%{_bindir}/magerun2

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
%{_bindir}/magerun2
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
* Tue Jul 22 2025 Danila Vershinin <info@getpagespeed.com> 9.0.2-1
- release 9.0.2

* Wed Jun 25 2025 Danila Vershinin <info@getpagespeed.com> 9.0.1-1
- release 9.0.1

* Tue Apr 29 2025 Danila Vershinin <info@getpagespeed.com> 8.1.1-1
- release 8.1.1

* Tue Feb 25 2025 Danila Vershinin <info@getpagespeed.com> 8.0.0-1
- release 8.0.0

* Tue Nov 26 2024 Danila Vershinin <info@getpagespeed.com> 7.5.0-1
- release 7.5.0

* Sat Apr 27 2024 Danila Vershinin <info@getpagespeed.com> 7.4.0-1
- release 7.4.0

* Thu Feb 01 2024 Danila Vershinin <info@getpagespeed.com> 7.3.1-1
- release 7.3.1

* Wed Oct 11 2023 Danila Vershinin <info@getpagespeed.com> 7.2.0-1
- release 7.2.0

* Tue Aug 01 2023 Danila Vershinin <info@getpagespeed.com> 7.1.0-1
- release 7.1.0

* Wed Apr 12 2023 Danila Vershinin <info@getpagespeed.com> 7.0.3-1
- release 7.0.3

* Sat Apr 01 2023 Danila Vershinin <info@getpagespeed.com> 7.0.2-1
- release 7.0.2

* Thu Mar 23 2023 Danila Vershinin <info@getpagespeed.com> 7.0.1-1
- release 7.0.1

* Tue Mar 14 2023 Danila Vershinin <info@getpagespeed.com> 7.0.0-1
- release 7.0.0

* Thu Jan 12 2023 Danila Vershinin <info@getpagespeed.com> 6.1.1-1
- release 6.1.1

* Thu Oct 20 2022 Danila Vershinin <info@getpagespeed.com> 6.1.0-1
- release 6.1.0

* Thu Sep 29 2022 Danila Vershinin <info@getpagespeed.com> 6.0.1-1
- release 6.0.1

* Sat Aug 06 2022 Danila Vershinin <info@getpagespeed.com> 5.2.0-1
- release 5.2.0

* Sat May 07 2022 Danila Vershinin <info@getpagespeed.com> 5.1.0-1
- release 5.1.0

* Thu Apr 21 2022 Danila Vershinin <info@getpagespeed.com> 5.0.2-1
- release 5.0.2

* Fri Apr 15 2022 Danila Vershinin <info@getpagespeed.com> 5.0.1-1
- release 5.0.1

* Wed Apr 13 2022 Danila Vershinin <info@getpagespeed.com> 5.0.0-1
- release 5.0.0

* Thu Dec 23 2021 Danila Vershinin <info@getpagespeed.com> 4.9.1-1
- release 4.9.1

* Wed Dec 22 2021 Danila Vershinin <info@getpagespeed.com> 4.9.0-1
- release 4.9.0

* Sun Dec 05 2021 Danila Vershinin <info@getpagespeed.com> 4.8.0-1
- release 4.8.0

* Tue Jul 06 2021 Danila Vershinin <info@getpagespeed.com> 4.7.0-1
- release 4.7.0

* Tue Jun 15 2021 Danila Vershinin <info@getpagespeed.com> 4.6.1-1
- release 4.6.1

* Sun Jun 13 2021 Danila Vershinin <info@getpagespeed.com> 4.6.0-1
- release 4.6.0

* Mon Feb 15 2021 Danila Vershinin <info@getpagespeed.com> 4.5.0-1
- release 4.5.0

* Sun Dec 06 2020 Danila Vershinin <info@getpagespeed.com> 4.4.0-1
- release 4.4.0

* Sat Sep 19 2020 Danila Vershinin <info@getpagespeed.com> 4.3.0-1
- release 4.3.0

* Sun Aug 23 2020 Danila Vershinin <info@getpagespeed.com> 4.2.0-1
- release 4.2.0

* Mon Apr 20 2020 Danila Vershinin <info@getpagespeed.com> 4.1.0-1
- release 4.1.0

* Wed Mar 25 2020 Danila Vershinin <info@getpagespeed.com> 4.0.4-1
- upstream version auto-updated to 4.0.4

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
