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
from .perpetualTimer import PerpetualTimer
import logging
import argparse
import threading
import queue

class Console:
    def __init__(self):
        self.logger = None
        self.in_file = None
        self.out_file = None
        self.num_of_threads = defines.NUM_OF_THREADS
        self.timeout = defines.TIMEOUT
        self.strategy = None
        self.write_interval = defines.WRITE_INTERVAL
        self.ssl_mode = False

        # Configure
        self.configure()

        # Read arguments
        self.parseArgs()

        # Start process
        self.run()

    def configure(self):
        self.logger = logging.getLogger(defines.LOGGER_NAME)
        self.logger.setLevel(logging.DEBUG)
        self.logger.disabled = True;

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
        parser.add_argument('-o', required=True, type=argparse.FileType('a'), help='Proxy list out file (append)')
        parser.add_argument('-t', default=defines.NUM_OF_THREADS, type=int, help='Number of threads')
        parser.add_argument('-x', default=defines.TIMEOUT, type=int, help='Timeout in sec')
        parser.add_argument('-w', default=defines.WRITE_INTERVAL, type=int, help='Write results to file interval in sec')
        parser.add_argument('-s', default=defines.DEFAULT_STRATEGY, choices=defines.STRATEGIES, help='Select strategy')
        parser.add_argument('-ssl', default="no", choices=['yes', 'no'], help='SSL Mode')
        parser.add_argument('-debug', default="no", choices=['yes', 'no'], help='Debug Mode')

        args = parser.parse_args()
        self.logger.debug(args)
        self.in_file = args.i
        self.out_file = args.o
        self.num_of_threads = args.t
        self.timeout = args.x
        self.strategy = args.s
        self.write_interval = args.w
        if args.ssl == "yes":
            self.ssl_mode = True
        if args.debug == "yes":
            self.logger.disabled = False

    def run(self):
        queue_lock = threading.Lock()
        work_queue = queue.Queue()
        threads = []
        results = []

        for i in range(self.num_of_threads):
            thread = Worker(i, "Worker-"+str(i), work_queue, self.timeout, self.strategy, self.ssl_mode, results)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)

        rows = list(map(lambda x: x.split(":"), [line.rstrip('\n') for line in self.in_file]))

        for row in rows:
            work_queue.put(Proxy(row[0], row[1]))

        def write_to_file(_results):
            # make copy of the results and reset the list
            local_results = list(_results)
            _results[:] = []
            out_rows = list(map(lambda x: '{0}:{1}'.format(x.host, x.port), local_results))
            [self.out_file.write('{0}\n'.format(line)) for line in out_rows]
            self.out_file.flush()
            self.logger.debug('[Write {0} results to file]'.format(len(local_results)))
            self.logger.debug(out_rows)
            if work_queue.empty() is True:
                writer.cancel()

        writer = PerpetualTimer(self.write_interval, write_to_file, results)
        writer.start()
        work_queue.join()
        writer.cancel()
        write_to_file(results)


if __name__ == "__main__":
    console = Console()
