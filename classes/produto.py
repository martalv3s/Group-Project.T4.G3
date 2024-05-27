from classes.gclass import Gclass
class Produto (Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1

    att =['_code','_nome','_cor','_tamanho', '_price', '_stock', 'foto']

    header = 'Produtos'

    des = ['Código', 'Nome', 'Cor', 'Tamanho', 'Preço', 'Stock', 'Foto']

    def __init__(self, code, nome, cor, tamanho, price, stock, foto):
        super().__init__()

        self._code = code
        self._nome = nome
        self._cor = cor
        self._tamanho = tamanho
        self._price = float(price)
        self._stock = int(stock)
        self._foto = foto

        Produto.obj[code] = self
        Produto.lst.append(code)

    @property
    def code (self):
        return self._code

    @property
    def nome (self) :
        return self._nome

    @property 
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock) :
        self._stock = stock
        
    @property
    def cor (self):
        return self._cor
    
    @property 
    def tamanho (self):
        return self._tamanho