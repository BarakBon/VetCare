import unittest
import dbcontrol
from dbcontrol import *


class dbcontrol(unittest.TestCase):

    def test_newcustomer(self):
        self.assertEqual(newcustomer('!MayaS','Maya676','Maya','Shalom','Dimona','0524168852','MayaS@ac.sce.as.il'
                                     ,'Customer'),-2,"Should be -2")
        self.assertEqual(newcustomer('OrB','OB26','Or','Bonker','Dimona','527379951','Orbo@ac.sce.ac.il','Customer'),
                         -1, "Should be -1")
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

    def test_AnimalName(self):
        self.assertTrue(AnimalName('5'), "Should be True")
        self.assertTrue(AnimalName('4'), "Should be Ture")
        self.assertEqual(AnimalName('10'),-1, "Should be False")

    def test_UserName(self):
       self.assertTrue(UserName('3'),"Should be True")
       self.assertTrue(UserName('6'),"Should be True")
       self.assertEqual(UserName('100'),-1,"Should be False")



if __name__ == '__main__':
    unittest.main()
