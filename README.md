MoceanAPI Client Library for Python 
============================

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
from mocean import Mocean, Client

token = Client("API_KEY_HERE", "API_SECRET_HERE")
mocean = Mocean(token)
```

## Example

To use [Mocean's SMS API][doc_sms] to send an SMS message, call the `mocean.sms.create().send()` method.

The API can be called directly, using a simple array of parameters, the keys match the [parameters of the API][doc_sms].

```python
res = mocean.sms.create({
    "mocean-from": "MOCEAN",
    "mocean-to": 60123456789,
    "mocean-text": "Hello World"
}).send()

print(res)
```
    
The API response data can be accessed as array properties of the message. 

```python
print("Sent message to {}. Message ID is {}".format(res.receiver, res.msgid))
```

License
-------

This library is released under the [MIT License][license]

[signup]: https://dashboard.moceanapi.com/register?medium=github&campaign=sdk-python
[doc_sms]: https://docs.moceanapi.com/?python#send-sms
[doc_inbound]: https://docs.moceanapi.com/?python#receive-sms
[doc_verify]: https://docs.moceanapi.com/?python#overview-3
[license]: LICENSE.txt