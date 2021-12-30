import unittest
import dbcontrol
from dbcontrol import *


class dbcontrol(unittest.TestCase):

    def test_newcustomer(self):
        #invalid symbol at the user name
        self.assertEqual(newcustomer('!MayaS','Maya676','Maya','Shalom','Dimona','0524168852','MayaS@ac.sce.as.il'
                                     ,'Customer'),-2,"Should be -2")
        #invalid email address
        self.assertEqual(newcustomer('MayaS', 'Maya676', 'Maya', 'Shalom', 'Dimona', '0524168852', '@ac.sce.as.il'
                                     , 'Customer'), -2, "Should be -2")
        #customer exist
        self.assertEqual(newcustomer('OrB','OB26','Or','Bonker','Dimona','527379951','Orbo@ac.sce.ac.il','Customer'),
                         -1, "Should be -1")

    def test_newAnimal(self):
        self.assertEqual(newAnimal('4','Do','Bob'), -2, "should be -2")
        self.assertEqual(newAnimal('a','Dog','Bob'), -2, "should be -2")
        self.assertEqual(newAnimal('4','Rabit','Felix'), -1, "should be -1")

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

    def test_Date_Check(self):
        self.assertIsNotNone(Date_Check('2021-10-05'),'Should be True')
        self.assertIsNotNone(Date_Check('2021-10-06'), 'Should be True')
        self.assertIsNotNone(Date_Check('2021-10-07'), 'Should be True')

    def test_retu_appoin(self):
        self.assertIsNotNone(retu_appoin('2021-12-20'), 'Should be True')
        self.assertIsNotNone(retu_appoin('2021-11-28'), 'Should be True')
        self.assertIsNotNone(retu_appoin('2022-01-02'), 'Should be True')

    def test_Show_appointment(self):
        self.assertIsNotNone(Show_appointment('2021-12-23'), 'Should be True')
        self.assertIsNotNone(Show_appointment('2022-12-17'), 'Should be True')
        self.assertIsNotNone(Show_appointment('2022-02-30'), 'Should be True')

    def test_get_important_note(self):
        self.assertEqual(get_important_note(2,'Gi'),-1,'Should be -1')
        self.assertEqual(get_important_note(3,'Simba'),'Alergic to bugs','Should be Alergic to bugs')
        self.assertEqual(get_important_note(2, 2), -1, 'Should be -1')

    def test_animal_details(self):
        self.assertEqual(animal_details(4,'Felix'),('Rabit', 'Felix', 'Blind'),"Should be ('Rabit', 'Felix', 'Blind')")
        self.assertEqual(animal_details(2,'Bob'), -1, "Should be -1")
        self.assertEqual(animal_details(2,2), -1, "Should be -1")

    def test_Animal_appointment(self):
        self.assertTrue(Animal_appointment('2021-10-05','5','Max'), "Should be True")
        self.assertFalse(Animal_appointment('2021-10-05', '5', 'Simba'), "Should be False")
        self.assertFalse(Animal_appointment('2021-12-27', '3', 'Simba'), "Should be False")

    def test_Customer_appointment(self):
        self.assertTrue(Customer_appointment('2021-10-05', '5'), "Should be True")
        self.assertFalse(Customer_appointment('2021-12-27', '3' ), "Should be False")
        self.assertFalse(Customer_appointment('2021-12-29', '6'), "Should be False")

    def test_get_treatment(self):
        self.assertIsNotNone(get_treatments('5','Max'),"Should be True")
        self.assertIsNot(get_treatments('1000','DC'),"Should be False")
        self.assertIsNot(get_treatments('8555','XXX'),"Should be False")


if __name__ == '__main__':
    unittest.main()
