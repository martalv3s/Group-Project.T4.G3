import datetime
from classes.cliente import Cliente
from classes.produto import Produto
from classes.gclass import Gclass

class Pedido(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1

    att = ['_code', '_codigo_cliente', '_quantity', '_date']

    header = 'Pedidos'

    des = ['Código Produto', 'Up', 'Quantidade', 'Data', 'Stock Atual']

    def __init__(self, code, codigo_cliente, quantity, date=None):
        super().__init__()
        print("Code", code)
        print("quantidade", quantity)
        if code == 'None':
            codes = Pedido.getatlist("_code")
            if codes == []:
                code = str(1)
            else:
                code = str(max(map(int, Pedido.getatlist('_code'))) + 1)

        if code in Produto.lst:
            produto = Produto.obj[code]
            quantity = int(quantity) if quantity else 0
            if produto.stock >= quantity:
                self._code = code
                self.date = datetime.date.today()
                self._codigo_cliente = codigo_cliente
                self.quantity = quantity
                self.stock_disponivel = produto.stock - quantity


                Pedido.obj[code] = self
                Pedido.lst.append(code)

                produto.stock -= quantity
            else:
                print('Stock insuficiente para o produto ', code)
        else:
            print('Produto ', code, ' não foi encontrado.')

    @property
    def code(self):
        return self._code

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def codigo_cliente(self):
        return self._codigo_cliente

    @codigo_cliente.setter
    def codigo_cliente(self, codigo):
        if codigo in Cliente.lst:
            self._codigo_cliente = codigo
        else:
            print('Cliente ', codigo, ' não foi encontrado.')

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity