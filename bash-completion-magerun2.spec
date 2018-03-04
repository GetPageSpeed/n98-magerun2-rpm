Summary: A bash completion helper for n98-magerun2
Name: bash-completion-magerun2
Version: 2.1.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://magerun.net/

Source0: https://github.com/netz98/n98-magerun2/archive/%{version}.tar.gz#/n98-magerun2-%{version}.tar.gz

BuildArch: noarch
Requires: bash-completion

%description
Install this package to enable tab-completion of functions and installed
modules with the magerun2 command.

%prep
%setup -n n98-magerun2-%{version}


%build
# Nothing to do

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
%{__install} -Dp -m0755 res/autocompletion/bash/n98-magerun2.phar.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

%post
. /etc/profile.d/bash_completion.sh

%postun
. /etc/profile.d/bash_completion.sh

%files
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/bash_completion.d/*

%changelog
* Sun Mar 4 2018 Danila Vershinin <info@getpagespeed.com> 2.1.2-1
- update to 2.1.2