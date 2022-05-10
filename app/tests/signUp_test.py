import unittest
from ..models import SignUp
 
def test__init__(self):
    self.new_signUp= SignUp("haimana","uta","haimana@gmail.com","12345678")
    
def test_save_signUp(self):
            self.new_signUp.save_signUp()
            self.assertEqual(len(SignUp.signUp_list),1)
            
if __name__=='__main__':
    unittest.main()