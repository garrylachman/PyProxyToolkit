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

from ..proxy import Proxy
from ..defines import defines
import logging

class StrategyAbstract:
    def __init__(self):
        self._url = None
        self.ssl_mode = False
        self.logger = logging.getLogger(defines.LOGGER_NAME)

    @property
    def url(self):
        return self._url

    def setSSLMode(self, ssl_mode):
        self.ssl_mode = ssl_mode

    def match(self, response, proxy: Proxy):
        pass