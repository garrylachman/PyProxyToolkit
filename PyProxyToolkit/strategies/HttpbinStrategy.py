from .strategyAbstract import StrategyAbstract
from ..proxy import Proxy
import json
import sys

class HttpbinStrategy(StrategyAbstract):
    def __init__(self):
        super(HttpbinStrategy, self).__init__()
        self.url = 'http://httpbin.org/ip'

    def match(self, response, proxy: Proxy):
        json_response = json.loads(response)
        try:
            return str(json_response['origin']).find(proxy.host) > -1
        except:
            self.logger.error(sys.exc_info()[0])

        return False
