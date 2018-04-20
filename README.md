# Sites Monitoring Utility

With this script you can check website health measuring two parameters: if the website is up and correctly responds over HTTP and if domain expires in less than a month.

# Quickstart

Specify the path to a file with URLs when using this script from the command line.

```bash
$ python check_sites_health.py <path to file>
```

### Example of script launch on Linux, Python 3.5:

```bash

$ python check_sites_health.py domains.txt
You are checking: https://google.com
Server is up
Domain expires in more than 30 days
You are checking: https://kenterior.com
Server is down
Domain is already expired
You are checking: https://googlemoogle.com
Server is down
Domain expires in more than 30 days
You are checking: https://googlegooglemoogle.com
Server is down
Domain name not found

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
