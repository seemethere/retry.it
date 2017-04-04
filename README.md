[![Travis](https://img.shields.io/travis/seemethere/retry.it.svg?maxAge=2592000)](https://travis-ci.org/seemethere/retry.it)
[![PyPI](https://img.shields.io/pypi/v/retry.it.svg?maxAge=2592000)](https://pypi.python.org/pypi/retry.it)
[![Documentation Status](https://readthedocs.org/projects/retryit/badge/?version=latest)](http://retryit.readthedocs.io/en/latest/?badge=latest)

# :arrows_counterclockwise: retry.it, a simple retry library
Ever wanted to retry a function but didn't want to implement fancy
logic to do it?

Well now you don't have to thanks to `retry.it`!

Thanks to this simple <100 line module you too can experience the wonders of
retrying functions in all of their glory, without any of the fancy logic!

Have a function that only works some of the time? **retry.it!**

Have a function that needs to poll a website `x` times to check if something is down? **retry.it!**

Have a function that you just want to run over and over again? **retry.it!**

NOTE: Compatability for Windows is not yet available

# Installation

```shell
pip install retry.it
```

# Features
* Functions can be retried based on:
  * Success criteria (like a status code not equaling 200)
  * Exceptions (like a function raising a requests.RequestException)
    * All accepted exceptions raise the original exception on failure as well!
* Functions can fail based on:
  * Maximum number of retries exceeded
  * Maximum timeout achieved
* Function retries can be spaced apart at a specific interval

# Examples

### Use it as a decorator!
Send a `GET` request to a URL until it returns a status code of 200!
Rest a second between tries
```python
import requests

from retry import retry

@retry(max_retries=-1, interval=1, success=lambda x: x.status_code == 200)
def poll_url(url, method='GET'):
    return requests.request(method, url)
```

### Use it with a timeout!
Same function as above, timeout after 10 seconds!
```python
import requests

from retry import retry

@retry(
    max_retries=-1, interval=1, success=lambda x: x.status_code == 200,
    timeout=10)
def poll_url(url, method='GET'):
    return requests.request(method, url)
```

### Use it with Exceptions!
Same function as above, timeout after 10 seconds!
```python
import requests

from retry import retry

@retry(
    exceptions=(requests.RequestException,), max_retries=-1, interval=1,
    success=lambda x: x.status_code == 200, timeout=10)
def poll_url(url, method='GET'):
    return requests.request(method, url)
```

### Use it as a wrapper!
Send any type of request to a URL until it returns a status code set by the
user!
```python
import requests

from retry import retry

def poll_url(url, method='GET'):
    return requests.request(method, url)

def poll_url_with_retries(
        url, method='GET', max_retries=-1, interval=1, status_code=200):
    return retry(
        max_retries=max_retries,
        interval=interval,
        success=lambda x: x.status_code == status_code
        timeout=10)(poll_url)(url, method)
```


# Contributing
1. Fork the repo
2. Commit changes to your Fork
3. Submit those changes!

# Why use retry.it
When looking for a library that does something similar to `retry.it`
I could not find one that not only suited everything I needed but also was
something I could understand and extend easily. Enter `retry.it`!
`retry.it` aims to be simple and clocking in at <100 lines of real code it is
simple!

# Alternatives
- [retrying](https://github.com/rholder/retrying)
- [retry](https://github.com/invl/retry)
