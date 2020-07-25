class Customer(object):
    """Online Customer pulled from database"""

    def __init__(self,name,username,password,address):
        self.name = name
        self.username = username
        self.password = password
        self.address = address

    def check_password(self, passwordAttempt):
        return(self.password == passwordAttempt)

    def _str_(self):
        return ('(n)ame: '+self.name+'\n(u)sername: '+self.username+'\n(p)assword: '+self.password+'\n(a)ddress: '+self.address)