[![Travis](https://img.shields.io/travis/seemethere/retry.it.svg?maxAge=2592000)](https://travis-ci.org/seemethere/retry.it)
[![PyPI](https://img.shields.io/pypi/v/retry.it.svg?maxAge=2592000)](https://pypi.python.org/pypi/retry.it)

# retry.it, a simple retry library
Ever wanted to retry a function but didn't want to implement fancy
logic to do it?

Well now you don't have to thanks to `retry.it`!

Thanks to this simple <100 line module you too can experience the wonders of
retrying functions in all of their glory, without any of the fancy logic!

Have a function that only works some of the time? **retry.it!**

Have a function that needs to poll a website `x` times to check if something is down? **retry.it!**

Have a function that you just want to run over and over again? **retry.it!**

# Installation

```shell
pip install retry.it
```

# Examples

Send a `GET` request to a URL until it returns a status code of 200!
Rest a second between tries
```python
import requests

from retry import retry

@retry(max_retries=-1, interval=1, success=lambda x: x.status_code == 200)
def poll_url(url, method='GET'):
    return requests.request(method, url)
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
- [retrying](https://github.com/rholder/retrying()
- [retry](https://github.com/invl/retry)
