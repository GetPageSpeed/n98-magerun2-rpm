# n98-magerun2-rpm

RPM builds of [`n98-magerun2`](https://github.com/netz98/n98-magerun2).

|CI|Purpose|Status|
|---|---|---|
|Travis|Tests buildability, deploys to PackageCloud|[![Build Status](https://travis-ci.org/GetPageSpeed/n98-magerun2-rpm.svg?branch=master)](https://travis-ci.org/GetPageSpeed/n98-magerun2-rpm)|
| CircleCI | Deploys [GetPageSpeed repository](https://www.getpagespeed.com/redhat) (fast CDN repo, RHEL 6+) | [![CircleCI](https://circleci.com/gh/GetPageSpeed/n98-magerun2-rpm.svg?style=svg)](https://circleci.com/gh/GetPageSpeed/n98-magerun2-rpm) |

## Installation (CentOS/RHEL 6+)

```bash
# First, install Remi's PHP >= 7.2

sudo yum -y install https://extras.getpagespeed.com/release-latest.rpm
sudo yum -y install n98-magerun2
```

