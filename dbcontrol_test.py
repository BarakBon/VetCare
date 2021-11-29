import unittest
import dbcontrol
from dbcontrol import *

class dbcontrol(unittest.TestCase):
    def test_Search(self):
        self.assertTrue(Search('OrB'), "Should be True")
        self.assertFalse(Search('222'), "Should be False")
        self.assertFalse(Search('Barak4B'), "Should be False")








    if __name__ == '__main__':
        unittest.main()