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
from .check import Check
from .strategies.httpbinStrategy import HttpbinStrategy
from .strategies.googleStrategy import GoogleStrategy
import logging
import threading

class Worker(threading.Thread):
    def __init__(self, threadID, name, q, timeout, strategy,results):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
        self.name = name
        self.results = results
        self.timeout = timeout

        if strategy == defines.HTTPBIN_STRATEGY:
            self.strategy = HttpbinStrategy()
        elif strategy == defines.GOOGLE_STRATEGY:
            self.strategy = GoogleStrategy()
        # Todo: rise exception if not stragegy found

        self.checker = Check(self.strategy, self.timeout)
        self.logger = logging.getLogger(defines.LOGGER_NAME)
        self.logger.debug("Start worker {0} ({1})".format(self.name, self.threadID))

    def run(self):
        while True:
            data = self.q.get()

            self.checker.check(data)
            msg = "Fail"
            if data.isValid is True:
                self.results.append(data)
                msg = "Ok"

            self.logger.debug("{3} - {0}:{1} - {2}".format(data.host, data.port, msg, self.name))

            self.q.task_done()