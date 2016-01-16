from .defines import defines
from .proxy import Proxy
from .check import Check
from .strategies.httpbinStrategy import HttpbinStrategy
import logging
import threading

class Worker(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
        self.name = name
        self.checker = Check(HttpbinStrategy())
        self.logger = logging.getLogger(defines.LOGGER_NAME)
        self.logger.debug("Start worker {0} ({1})".format(self.name, self.threadID))

    def run(self):
        while True:
            data = self.q.get()

            self.checker.check(data)
            msg = "Fail"
            if data.isValid is True:
                msg = "Ok"

            self.logger.debug("{3} - {0}:{1} - {2}".format(data.host, data.port, msg, self.name))

            self.q.task_done()