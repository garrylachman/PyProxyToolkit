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

import unittest
import sys

from PyProxyToolkit import Console

class ConsoleCase(unittest.TestCase):
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(ConsoleCase('test_properties'))
        return suite

    def setUp(self):
        self.threads = 5;
        self.timeout = 10
        self.strategy = 'googleStrategy'
        sys.argv = [sys.argv[0], '-i=in.txt', '-o=out.txt', '-t='+str(self.threads), '-x='+str(self.timeout), '-s='+str(self.strategy)]
        self.console = Console.Console()

    def test_properties(self):
        self.assertEquals(self.console.inFile.name, "in.txt")
        self.assertEquals(self.console.outFile.name, "out.txt")
        self.assertEquals(self.console.numOfThreads, self.threads)
        self.assertEquals(self.console.timeout, self.timeout)
        self.assertEquals(self.console.strategy, self.strategy)

if __name__ == '__main__':
    unittest.main()
