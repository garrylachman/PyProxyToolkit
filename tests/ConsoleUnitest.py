import unittest
import sys

from PyProxyToolkit import Console

class ConsoleCase(unittest.TestCase):
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(ConsoleCase('test_properties'))
        return suite

    def setUp(self):
        self.threads = 2;
        sys.argv = [sys.argv[0], '-i=in.txt', '-o=out.txt', '-t='+str(self.threads)]
        self.console = Console.Console()

    def test_properties(self):
        self.assertEquals(self.console.inFile.name, "in.txt")
        self.assertEquals(self.console.outFile.name, "out.txt")
        self.assertEquals(self.console.numOfTheads, self.threads)

if __name__ == '__main__':
    unittest.main()
