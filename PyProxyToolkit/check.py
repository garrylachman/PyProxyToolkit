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

from .defines import defines
from .proxy import Proxy
from .strategies.strategyAbstract import StrategyAbstract
from .strategies.httpbinStrategy import HttpbinStrategy
from .strategies.httpbinAnonymousStrategy import HttpbinAnonymousStrategy
import logging
import http
import urllib.request, urllib.parse, urllib.error
import sys

class Check:
    def __init__(self, strategy: StrategyAbstract, timeout):
        self.strategy = strategy
        self.timeout = timeout
        self.logger = logging.getLogger(defines.LOGGER_NAME)

    def check(self, proxy: Proxy):
        proxy_provider = urllib.request.ProxyHandler({
            'http': '{0}:{1}'.format(proxy.host, str(proxy.port)),
            'https': '{0}:{1}'.format(proxy.host, str(proxy.port))
        })
        opener = urllib.request.build_opener(proxy_provider)
        opener.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
        ]

        res = None
        try:
            res = opener.open(self.strategy.url, timeout=self.timeout)
        except urllib.error.URLError as e:
            self.logger.error(e)
            proxy.isValid = False
            if res is not None:
                res.close()
            return False
        except http.client.HTTPException as e:
            self.logger.error(e)
            proxy.isValid = False
            if res is not None:
                res.close()
            return False
        except:
            self.logger.error(sys.exc_info()[0])
            proxy.isValid = False
            if res is not None:
                res.close()
            return False

        response=''
        while True:
            try:
                responsePart = res.read()
            except http.client.IncompleteRead as icread:
                try:
                    response = response + icread.partial.decode('utf-8')
                except:
                    self.logger.error(sys.exc_info()[0])
                    proxy.isValid = False
                    res.close()
                    return False
                continue
            else:
                try:
                    response = response + responsePart.decode('utf-8')
                except:
                    self.logger.error(sys.exc_info()[0])
                    proxy.isValid = False
                    res.close()
                    return False
            break

        res.close()
        proxy.isValid = self.strategy.match(response, proxy)
        return proxy.isValid