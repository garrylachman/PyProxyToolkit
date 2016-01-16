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

class Proxy:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.isValid = False

    @property
    def isValid(self):
        return self.__isValid

    @isValid.setter
    def isValid(self, value):
        self.__isValid = value