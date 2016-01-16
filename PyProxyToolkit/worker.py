from .defines import defines
import logging
import threading

class Worker(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
        self.name = name
        self.logger = logging.getLogger(defines.LOGGER_NAME)
        self.logger.debug("Start worker {0} ({1})".format(self.name, self.threadID))

    def run(self):
        while True:
            data = self.q.get()

            host = data['host']
            port = data['port']
            msg = "OK"
            self.logger.debug("{3} - {0}:{1} - {2}".format(host, port, msg, self.name))

            self.q.task_done()