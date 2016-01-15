import unittest
import sys

from PyProxyToolkit import Console

class ConsoleCase(unittest.TestCase):
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(ConsoleCase('test_properties'))
        return suite

    def setUp(self):
        sys.argv = [sys.argv[0], '-i=in.txt', '-o=out.txt', '-t=10']
        self.console = Console.Console()

    def test_properties(self):
        self.assertEquals(self.console.inFile.name, "in.txt")
        self.assertEquals(self.console.outFile.name, "out.txt")
        self.assertEquals(self.console.numOfTheads, 10)

if __name__ == '__main__':
    unittest.main()
