class Login:
    
    
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password
        
        
class SignUp:
    pass
    signUp_list =[]

    def __init__(self):
        self.assertEqual(self.new_login.fname,"haimana")
        self.assertEqual(self.new_login.lname,"uta")
        self.assertEqual(self.new_login.email_address, "haimana@gmail.com")
        self.assertEqual(self.new_login.password,"12345678")
         
    def save_signUp(self):
        SignUp.signUp_list.append(self)
         
        
       