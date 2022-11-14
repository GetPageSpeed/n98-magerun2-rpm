#!/bin/bash

RHEL=$(rpm -E 0%{?rhel})
FEDORA=$(rpm -E 0%{?fedora})
yum -y install http://rpms.remirepo.net/enterprise/remi-release-${RHEL}.rpm

# n98-magerun2 supports only PHP 7.2 and above
if [[ "${RHEL}" -ge "8" ]] || [[ "${FEDORA}" -ge "33" ]]; then
  dnf -y install yum-utils
  dnf -y module reset php
  dnf -y module install php:remi-7.4
  # new composer is in there:
  dnf config-manager --enable remi
  dnf -y install composer
  dnf -y update composer
else
  REPO=remi-php74
  yum -y install yum-utils
  yum-config-manager --enable remi
  yum-config-manager --enable ${REPO}
fi

# php-pear-phing in remi is no good
# no dependencies in EL8 for php-pear-phing, using phing's phar
if [[ "${RHEL}" -le "7" ]]; then
  yum -y install --disablerepo=remi* php-pear-phing
  # ensure upgrading system PHP to 7.4
  yum -y upgrade
fi

echo "phar.readonly=0" >> /etc/php.ini