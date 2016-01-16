from .defines import defines
from .proxy import Proxy
from .strategies.strategyAbstract import StrategyAbstract
from .strategies.httpbinStrategy import HttpbinStrategy
import logging
import http
import urllib.request, urllib.parse, urllib.error

class Check:
    def __init__(self, strategy: StrategyAbstract):
        self.strategy = strategy
        self.logger = logging.getLogger(defines.LOGGER_NAME)

    def check(self, proxy: Proxy):
        proxy_provider = urllib.request.ProxyHandler({'http': 'http://{0}:{1}'.format(proxy.host, str(proxy.port))})
        opener = urllib.request.build_opener(proxy_provider)

        try:
            res = opener.open(self.strategy.url)
        except urllib.error.URLError as e:
            self.logger.error(e)
            proxy.isValid = False
            return False
        except http.client.HTTPException as e:
            self.logger.error(e)
            proxy.isValid = False
            return False
        except:
            self.logger.error('Load Error')
            proxy.isValid = False
            return False

        response=''
        while True:
            try:
                responsePart = res.read()
            except http.client.IncompleteRead as icread:
                try:
                    response = response + icread.partial.decode('utf-8')
                except:
                    self.logger.error("Error - Parse")
                    proxy.isValid = False
                    return None
                continue
            else:
                try:
                    response = response + responsePart.decode('utf-8')
                except:
                    self.logger.error("Error - Parse")
                    proxy.isValid = False
                    return None
            break

        proxy.isValid = self.strategy.match(response, proxy)
        return proxy.isValid