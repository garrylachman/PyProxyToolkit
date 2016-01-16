from ..proxy import Proxy
from ..defines import defines
import logging

class StrategyAbstract:
    def __init__(self):
        self.url = None
        self.logger = logging.getLogger(defines.LOGGER_NAME)

    def match(self, response, proxy: Proxy):
        pass