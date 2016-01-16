import unittest
import sys

from PyProxyToolkit import console

class ConsoleCase(unittest.TestCase):
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(ConsoleCase('test_properties'))
        return suite

    def setUp(self):
        self.threads = 5;
        self.timeout = 10
        sys.argv = [sys.argv[0], '-i=in.txt', '-o=out.txt', '-t='+str(self.threads), '-x='+str(self.timeout)]
        self.console = console.Console()

    def test_properties(self):
        self.assertEquals(self.console.inFile.name, "in.txt")
        self.assertEquals(self.console.outFile.name, "out.txt")
        self.assertEquals(self.console.numOfThreads, self.threads)
        self.assertEquals(self.console.timeout, self.timeout)

if __name__ == '__main__':
    unittest.main()
