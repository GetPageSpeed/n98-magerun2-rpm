#!/bin/bash

yum -y install bc
RHEL=$(rpm -E 0%{?rhel} | bc)
FEDORA=$(rpm -E 0%{?fedora} | bc)
yum -y install http://rpms.remirepo.net/enterprise/remi-release-${RHEL}.rpm

# n98-magerun2 9.x requires PHP >= 8.1
if [[ "${RHEL}" -ge "8" ]] || [[ "${FEDORA}" -ge "33" ]]; then
  dnf -y install yum-utils
  dnf -y module reset php
  dnf -y module install php:remi-8.2
  # new composer is in there:
  dnf config-manager --enable remi
  dnf -y install composer
  dnf -y update composer
else
  REPO=remi-php82
  yum -y install yum-utils
  yum-config-manager --enable remi
  yum-config-manager --enable ${REPO}
  # ensure upgrading system PHP to 8.2
  yum -y upgrade
fi

echo "phar.readonly=0" >> /etc/php.ini