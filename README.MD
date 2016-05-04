#Python 3 Proxy Tookit - Fast Proxy Checker
Fast multi-threaded proxy checker based on strategies.

Copyright (C) 2016 Garry Lachman <garry@lachman.co> under GNU LGPL

https://rev.proxies.online

**Strategies:** *httpbinStrategy* (validate ip, default), *httpbinAnonymousStrategy* (validate ip - anonymous only, default), *googleStrategy* (validate if banned on google)

##Installing
Download the source code from github and run:

```
python3 setup.py install
```
or
```
pip3 install PyProxyToolkit
```


##Using
```
python3 -m PyProxyToolkit.Console -h
usage: Console.py [-h] -i I -o O [-t T] [-x X]
                   [-s {httpbinStrategy,googleStrategy}]

PyProxyChecker

optional arguments:
  -h, --help            show this help message and exit
  -i I                  Proxy list in file
  -o O                  Proxy list out file (append)
  -t T                  Number of threads
  -x X                  Timeout in sec
  -w W                  Write results to file interval in sec
  -s {httpbinStrategy,googleStrategy,httpbinAnonymousStrategy}
                        Select strategy
  -ssl {yes,no}         SSL Mode
  -debug {yes,no}       Debug Mode
```
example

```
python3 -m PyProxyToolkit.Console -i in.txt -o out.txt -t 30 -X 30 -s googleStrategy
```

##Write results interval
with -w option you can select the interval bewteen results output to file.
when working on big proxies list you might want to see the results while proxy checker working.
the default values is 30 sec.

##Strategies
Strategy provide the request url and matching logic.
The checker sends request to strategy url and return the content for validation.

Supported strategies:

 1. **httpbinStrategy** - the strategy and sends request to ```http://httpbin.org/ip``` and validate the proxy ip against the response.
 2. **httpbinAnonymousStrategy** - same as httpbinStrategy buy filter out transparent proxies.
 3. **googleStrategy** - the strategy validate if the proxy is banned on Google


##Licence
Copyright (C) 2016 Garry Lachman <garry@lachman.co>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License version 2.1, as published by the Free Software Foundation.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.
