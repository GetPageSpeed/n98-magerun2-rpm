# magerun2-rpm

Travis deploys to packagecloud: [![Build Status](https://travis-ci.org/GetPageSpeed/n98-magerun2-rpm.svg?branch=master)](https://travis-ci.org/GetPageSpeed/wrk-rpm)
CircleCI deploys to GetPageSpeed repository: [![CircleCI](https://circleci.com/gh/GetPageSpeed/n98-magerun2-rpm/tree/master.svg?style=svg)](https://circleci.com/gh/GetPageSpeed/n98-magerun2-rpm/tree/master)

## Installation (CentOS/RHEL 6+)

```bash
sudo yum install https://extras.getpagespeed.com/release-el$(rpm -E %{rhel})-latest.rpm
sudo yum install n98-magerun2
```

