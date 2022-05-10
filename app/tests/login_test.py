import unittest
from app  import Login

class Testcaselogin(unittest.TestCase):
    def setUp(self):
     self.new_login= Login("haimana@gmail.com","12345678")# login object
     
     def __init__(self):
         self.assertEqual(self.new_login.email_address, "haimana@gmail.com")
         self.assertEqual(self.new_login.password,"12345678")
         
         
         
if __name__=='__main__':
    unittest.main()