import unittest
import dbcontrol
from dbcontrol import *

class dbcontrol(unittest.TestCase):
    def test_newcustomer(self):
        self.assertTrue(newcustomer('dana1','aaa1','dana','levi','Omer','0546357761','dana@gmail.com','Customer'), "Should be True")
        self.assertTrue(newcustomer(11,'dd','or','bok','djjk','9990','fdf','dfd'), "Should be True")
        self.assertNotEqual(newcustomer('MoriyaP', 'MP999', 'Moriya', 'Panker', 'Beer Sheva', '0526846251', 'Moriypa@ac.sce.ac.il', 'Customer'), "Should be Not Equal")

    if __name__ == '__main__':
        unittest.main()