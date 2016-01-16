#!/usr/bin/env python

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
from .worker import Worker
from .proxy import Proxy
import logging
import argparse
import threading
import queue

class Console:
    def __init__(self):
        self.inFile=None
        self.outFile=None
        self.numOfThreads=defines.NUM_OF_THREADS
        self.timeout=defines.TIMEOUT

        # Configure
        self.configure()

        # Read arguments
        self.parseArgs()

        # Start process
        self.run()

    def configure(self):
        self.logger = logging.getLogger(defines.LOGGER_NAME)
        self.logger.setLevel(logging.DEBUG)

        # create file handler which logs even debug messages
        fh = logging.FileHandler(defines.LOGGER_FILE)
        fh.setLevel(logging.ERROR)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def parseArgs(self):
        parser = argparse.ArgumentParser(description='PyProxyChecker')
        parser.add_argument('-i', required=True, type=argparse.FileType('r'), help='Proxy list in file')
        parser.add_argument('-o', required=True, type=argparse.FileType('w'), help='Proxy list out file')
        parser.add_argument('-t', default=defines.NUM_OF_THREADS, type=int, help='Number of threads')
        parser.add_argument('-x', default=defines.TIMEOUT, type=int, help='Timeout in sec')

        args = parser.parse_args()
        self.logger.debug(args)
        self.inFile = args.i
        self.outFile = args.o
        self.numOfThreads = args.t
        self.timeout = args.x

    def run(self):
        queue_lock = threading.Lock()
        work_queue = queue.Queue()
        threads = []
        results = []

        for i in range(self.numOfThreads):
            thread = Worker(i, "Worker-"+str(i), work_queue, self.timeout, results)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)

        rows = list(map(lambda x: x.split(":"), [line.rstrip('\n') for line in self.inFile]))

        for row in rows:
            work_queue.put(Proxy(row[0], row[1]))

        work_queue.join()

        out_rows = list(map(lambda x: '{0}:{1}'.format(x.host, x.port), results))
        [self.outFile.write('{0}\n'.format(line)) for line in out_rows]
        self.logger.debug(out_rows)


if __name__ == "__main__":
    console = Console()
