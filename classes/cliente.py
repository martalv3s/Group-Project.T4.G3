from classes.gclass import Gclass
class Cliente (Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_code','_nome','_email', '_password']
    header = 'Cliente'
    des = ['Code: ', 'Nome: ', 'Email: ', 'Password: ']
    
    def __init__ (self, code, nome, email, password):
        super().__init__()
        self._code = code
        self._nome = nome
        self._email = email
        self._password = password
        Cliente.obj[code] = self
        Cliente.lst.append(code)
    
    @property 
    def code (self):
        return self._code
    
    @property 
    def nome (self):
        return self._nome
    
    @property 
    def email (self):
        return self._email
    
    @property 
    def password (self):
        return self._password
    
    @password.setter
    def password (self, new_password):
        self._password = new_password
        
    def username (self):
        lista = list(map(str, self._nome.split(' ')))
        username = lista[0]
        return username
    
    # def chk_validity(self):
    #     message = 'Approved!'
    #     # Verifica o espaço do evento
    #     if self._venue_code in Venue.obj.keys():
    #         self._venue = Venue.obj[str(self._venue_code)]
    #         print(self._venue)
    #     else:
    #         message = 'Venue not found!'
    #         return message
    #     # Verifica o tipo do evento
    #     if self._type_code in Type.obj.keys():
    #         self._type = Type.obj[str(self._type_code)]
    #     else:
    #         message = 'Type not found!'
    #         return message
    #     # Verifica se o número de slots é superior à capacidade do espaço
    #     if int(self._slots) <= self._venue.capacity:
    #         self._slots = int(self._slots)
    #     else:
    #         message = "The selected venue isn't big enough!"
    #         return message
    #     return message
        