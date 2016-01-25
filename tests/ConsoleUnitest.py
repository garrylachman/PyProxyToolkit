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
        self.threads = 2
        self.timeout = 10
        self.write_interval=5
        self.strategy = 'httpbinAnonymousStrategy'
        sys.argv = [sys.argv[0],
                    '-i=in.txt',
                    '-o=out.txt',
                    '-t='+str(self.threads),
                    '-x='+str(self.timeout),
                    '-s='+str(self.strategy),
                    '-w='+str(self.write_interval),
                    '-ssl=yes']
        self.console = Console.Console()

    def test_properties(self):
        self.assertEquals(self.console.in_file.name, "in.txt")
        self.assertEquals(self.console.out_file.name, "out.txt")
        self.assertEquals(self.console.num_of_threads, self.threads)
        self.assertEquals(self.console.timeout, self.timeout)
        self.assertEquals(self.console.strategy, self.strategy)
        self.assertEquals(self.console.write_interval, self.write_interval)

if __name__ == '__main__':
    unittest.main()
