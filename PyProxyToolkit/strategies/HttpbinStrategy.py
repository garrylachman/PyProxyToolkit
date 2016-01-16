from .strategyAbstract import StrategyAbstract
from ..proxy import Proxy
import json


class HttpbinStrategy(StrategyAbstract):
    def __init__(self):
        super(HttpbinStrategy, self).__init__()
        self.url = 'http://httpbin.org/ip'

    def match(self, response, proxy: Proxy):
        json_response = json.loads(response)
        try:
            return json_response['origin'] == proxy.host
        except:
            self.logger.error("{0} - {1}:{2}".format(response, proxy.host, str(proxy.port)))

        return False
