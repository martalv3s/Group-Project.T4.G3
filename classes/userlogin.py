import bcrypt
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1

    att = ['_user','_usergroup','_password', '_up']

    header = 'Users'
   
    des = ['User','User group','Password', 'Up']
    username = ''

    def __init__(self, user, usergroup, password, up):
        super().__init__()
        self._user = user
        self._usergroup = usergroup
        self._password = password
        self._up = up
        
        Userlogin.obj[user] = self
        Userlogin.lst.append(user)

    
    @property
    def user(self):
        return self._user
    
    @property
    def usergroup(self):
        return self._usergroup
    
    @usergroup.setter
    def usergroup(self, usergroup):
        self._usergroup = usergroup
        
    @property
    def password(self):
        return ""
    
    @password.setter
    def password(self, password):
        self._password = password
        
    @property
    def user(self):
        return self._user

    @classmethod
    def chk_password(self, user, password):
        Userlogin.username =""
        if user in Userlogin.obj:
            obj = Userlogin.obj[user]
            valid = bcrypt.checkpw(password.encode(), obj._password.encode())
            message = "Valid"
            if not valid:
                message = 'Password incorreta'
        else:
            message = 'O utilizador não existe'
        return message
    
    @classmethod
    def set_password(self, password):
        passencrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return passencrypted.decode()
    
    def check(up):
        message = 'Válido'
        if len(up) != 9:
            message = 'UP deve ter 9 digitos!'
            return message
        return message
    