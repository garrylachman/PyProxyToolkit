"""
Copyright (C) 2016 Garry Lachman garry@lachman.co under GNU LGPL
https://github.com/garrylachman/PyProxyToolkit
https://rev.proxies.online

This library is free software; you can redistribute it and/or modify it under the terms of the
GNU Lesser General Public License version 2.1, as published by the Free Software Foundation.

This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Lesser General Public License for more details.
"""

def defines():
    defines.LOGGER_NAME = 'PyProxyToolkit'
    defines.LOGGER_FILE = 'py_proxy_toolkit.log'
    defines.NUM_OF_THREADS = 5
    defines.TIMEOUT = 30
    defines.HTTPBIN_STRATEGY = "httpbinStrategy"
    defines.GOOGLE_STRATEGY = "googleStrategy"
    defines.HTTPBIN_ANONYMOUS_STRATEGY = "httpbinAnonymousStrategy"
    defines.DEFAULT_STRATEGY = defines.HTTPBIN_STRATEGY
    defines.STRATEGIES = [defines.HTTPBIN_STRATEGY, defines.GOOGLE_STRATEGY, defines.HTTPBIN_ANONYMOUS_STRATEGY]
    defines.WRITE_INTERVAL = 30

defines()