from classes.pedido import Pedido
from classes.produto import Produto
from classes.gclass import Gclass


class Carrinho(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    key = 2
    att = ['code_pedido', 'code_produto', 'quantidade', 'preco']
    header = 'Carrinho'
    des = ['Código pedido', 'Código produto', 'Quantidade', 'Preco']

    def __init__(self, order_code, product_code, quantity, price):
        super().__init__()
        if order_code in Pedido.lst:
            if product_code in Produto.lst:
                self._order_code = order_code
                self._product_code = product_code
                self._quantity = float(quantity)
                self._price = float(price)

                produto = Produto.obj[product_code]
                if produto.stock >= quantity:  # Verifique se há estoque suficiente
                    # Reduza o stock do produto
                    produto.stock -= quantity

                    code = str(order_code) + str(product_code)
                    Carrinho.obj[code] = self
                    Carrinho.lst.append(code)
                else:
                    print('Estoque insuficiente para o produto ', product_code)
            else:
                print('Produto ', product_code, ' não foi encontrado.')
        else:
            print('Pedido ', order_code, ' não foi encontrado.')

    @property
    def order_code(self):
        return self._order_code

    @property
    def product_code(self):
        return self._product_code

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = float(quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = float(price)
