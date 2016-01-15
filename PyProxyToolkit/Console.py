#!/usr/bin/env python

from .defines import defines
import logging
import argparse

class Console:
    def __init__(self):
        self.inFile=None
        self.outFile=None
        self.numOfTheads=defines.NUM_OF_THREADS
        self.configure()
        self.logger.debug(__name__ + " init")
        self.parseArgs()

    def configure(self):
        self.logger = logging.getLogger(defines.LOGGER_NAME)
        self.logger.setLevel(logging.DEBUG)

        # create file handler which logs even debug messages
        fh = logging.FileHandler(defines.LOGGER_FILE)
        fh.setLevel(logging.DEBUG)

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

        args = parser.parse_args()
        self.logger.debug(args)
        self.inFile = args.i
        self.outFile = args.o
        self.numOfTheads = args.t




if __name__ == "__main__":
    console = Console()
