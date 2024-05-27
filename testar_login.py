from datafile import filename
from classes.userlogin import Userlogin

Userlogin.read(filename + 'business.db')

obj = Userlogin.from_string("kika;admin;1234")

print("objeto sem estar gravado ",obj)

Userlogin.insert(getattr(obj,Userlogin.att[0]))

obj = Userlogin.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "kika"
Userlogin.update(getattr(obj, Userlogin.att[0]))

Userlogin.read(filename + 'business.db')

print("\nobjectos gravados")    
for code in Userlogin.lst:
    print(Userlogin.obj[code])