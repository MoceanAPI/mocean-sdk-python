MoceanAPI Client Library for Python 
============================
[![Latest Stable Version](https://img.shields.io/pypi/v/moceansdk.svg)](https://pypi.org/project/moceansdk/)
[![Build Status](https://img.shields.io/travis/com/MoceanAPI/mocean-sdk-python.svg)](https://travis-ci.com/MoceanAPI/mocean-sdk-python)
[![codecov](https://img.shields.io/codecov/c/github/MoceanAPI/mocean-sdk-python.svg)](https://codecov.io/gh/MoceanAPI/mocean-sdk-python)
[![codacy](https://img.shields.io/codacy/grade/7ec97a7559f146928875fdaf28e1882e.svg)](https://app.codacy.com/project/MoceanAPI/mocean-sdk-python/dashboard)
[![license](https://img.shields.io/pypi/l/moceansdk.svg)](https://pypi.org/project/moceansdk/)

This is the Python client library for use Mocean's API. To use this, you'll need a Mocean account. Sign up [for free at 
moceanapi.com][signup].

 * [Installation](#installation)
 * [Usage](#usage)
 * [Examples](#examples)

## Installation

To use the client library you'll need to have [created a Mocean account][signup]. 

Install from PyPi using pip, a package manager for Python.

```bash
pip install moceansdk
```

## Usage

Create a client with your API key and secret:

```python
from moceansdk import Client, Basic

credential = Basic("API_KEY_HERE", "API_SECRET_HERE")
mocean = Client(credential)
```

## Example

To use [Mocean's SMS API][doc_sms] to send an SMS message, call the `mocean.sms.send()` method.

The API can be called directly, using a simple array of parameters, the keys match the [parameters of the API][doc_sms].

```python
res = mocean.sms.send({
    "mocean-from": "MOCEAN",
    "mocean-to": 60123456789,
    "mocean-text": "Hello World"
})

print(res)
```

### Responses

For your convenient, the API response has been parsed to `dict` using [dotmap](https://github.com/drgrib/dotmap) package.

```python
print(res)           # show full response string
print(res.status)    # show response status, '0' in this case
print(res['status']) # same as above

```

## Documentation

Kindly visit [MoceanApi Docs][doc_main] for more usage

License
-------

This library is released under the [MIT License][license]

[signup]: https://dashboard.moceanapi.com/register?medium=github&campaign=sdk-python
[doc_main]: https://moceanapi.com/docs/?python
[doc_sms]: https://moceanapi.com/docs/?python#send-sms
[license]: LICENSE.txt