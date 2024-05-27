from datafile import filename
from classes.cliente import Cliente

Cliente.read(filename + 'business.db')

obj = Cliente.from_string("cod123;marta;up202304679;up202304679@up.pt;1234")

print("objeto sem estar gravado ",obj)

Cliente.insert(getattr(obj,Cliente.att[0]))

obj = Cliente.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "marta"
Cliente.update(getattr(obj, Cliente.att[0]))

Cliente.read(filename + 'business.db')

print("\nobjectos gravados")    
for code in Cliente.lst:
    print(Cliente.obj[code])
    
    