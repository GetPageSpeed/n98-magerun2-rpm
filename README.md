# n98-magerun2-rpm

|CI|Purpose|Status|
|---|---|---|
|Travis|Tests buildability, deploys to PackageCloud|[![Build Status](https://travis-ci.org/GetPageSpeed/n98-magerun2-rpm.svg?branch=master)](https://travis-ci.org/GetPageSpeed/n98-magerun2-rpm)|
| CircleCI | Deploys [GetPageSpeed repository](https://www.getpagespeed.com/redhat) (fast CDN repo, RHEL 6+) | [![CircleCI](https://circleci.com/gh/GetPageSpeed/n98-magerun2-rpm.svg?style=svg)](https://circleci.com/gh/GetPageSpeed/n98-magerun2-rpm) |

## Installation (CentOS/RHEL 6+)

```bash
sudo yum install https://extras.getpagespeed.com/release-el$(rpm -E %{rhel})-latest.rpm
sudo yum install n98-magerun2
```

