#!/bin/bash

RHEL=$(rpm -E %{rhel})

yum -y install http://rpms.remirepo.net/enterprise/remi-release-${RHEL}.rpm

# n98-magerun2 supports only PHP 7.2 and above
if [[ "${RHEL}" -ge "8" ]]; then
  dnf -y install yum-utils
  dnf -y module reset php
  dnf -y module install php:remi-7.2
  # composer is in there:
  dnf config-manager --enable remi
else
  REPO=remi-php72
  yum -y install yum-utils
  yum-config-manager --enable remi
  yum-config-manager --enable ${REPO}
fi

# php-pear-phing in remi is no good
# no dependencies in EL8 for php-pear-phing, using phing's phar
if [[ "${RHEL}" -le "7" ]]; then
  yum -y install --disablerepo=remi* php-pear-phing
fi

echo "phar.readonly=0" >> /etc/php.ini