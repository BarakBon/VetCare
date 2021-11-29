import unittest
import dbcontrol
from dbcontrol import *

class dbcontrol(unittest.TestCase):
    def test_newcustomer(self):
        self.assertTrue(newcustomer('dana1','aaa1','dana','levi','Omer','0546357761','dana@gmail.com','Customer'), "Should be True")
        self.assertTrue(newcustomer(11,'dd','or','bok','djjk','9990','fdf','dfd'), "Should be True")
        self.assertNotEqual(newcustomer('MoriyaP', 'MP999', 'Moriya', 'Panker', 'Beer Sheva', '0526846251', 'Moriypa@ac.sce.ac.il', 'Customer'), "Should be Not Equal")
    def test_Login_check(self):
        self.assertFalse(Login_check('OrB', 'OE2'), "Should be False")
        self.assertTrue(Login_check('OrB', 'OB26'), "Should be True")
        self.assertFalse(Login_check('233', 'OE2'), "Should be False")
    def test_UserID_to_First_Name(self):
        self.assertTrue(UserID_to_First_Name('2'), "Should be True")
        self.assertFalse(UserID_to_First_Name('0'), "Should be False")
        self.assertFalse(UserID_to_First_Name('m'), "Should be False")
    def test_UserID_to_UserType(self):
        self.assertTrue(UserID_to_UserType('2'), "Should be True")
        self.assertFalse(UserID_to_First_Name('0'), "Should be False")
        self.assertFalse(UserID_to_First_Name('p'), "Should be False")
    def test_Search(self):
        self.assertTrue(Search('OrB'), "Should be True")
        self.assertFalse(Search('222'), "Should be False")
        self.assertFalse(Search('Barak4B'), "Should be False")


    if __name__ == '__main__':
        unittest.main()