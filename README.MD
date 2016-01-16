#Python 3 Proxy Tookit - Fast Proxy Checker
Fast multi-threaded proxy checker based on strategies.
Currently only 1 strategy is implemented but its very simple add custom one.

Copyright (C) 2016 Garry Lachman <garry@lachman.co> under GNU LGPL

https://rev.proxies.online

**Strategies:** *httpbinStrategy* (validate ip, default), *googleStrategy* (validate if banned on google)

##Installing
Download the source code from github and run:

```
python3 setup.py install
```

##Using
```
python3 -m PyProxyToolkit.Console -h
usage: Console.py [-h] -i I -o O [-t T] [-x X]
                   [-s {httpbinStrategy,googleStrategy}]

PyProxyChecker

optional arguments:
  -h, --help  show this help message and exit
  -i I        Proxy list in file
  -o O        Proxy list out file
  -t T        Number of threads
  -x X        Timeout in sec
  -s {httpbinStrategy,googleStrategy}
                        Select strategy - httpbinStrategy,googleStrategy
```
example

```
python3 -m PyProxyToolkit.Console -i in.txt -o out.txt -t 30 -X 30 -s googleStrategy
```

##Strategies
Strategy provide the request url and matching logic.
The checker sends request to strategy url and return the content for validation.

Supported strategies:

 1. httpbin - the strategy and sends request to ```http://httpbin.org/ip``` and validate the proxy ip against the response.
 2. google - the strategy validate if the proxy is banned on Google


##Licence
Copyright (C) 2016 Garry Lachman <garry@lachman.co>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License version 2.1, as published by the Free Software Foundation.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.
