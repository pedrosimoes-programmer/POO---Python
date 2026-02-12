from markdown_it.rules_block import table
from rich import print
from rich.table import Table


class Produto():
    def __init__(self, nome="", preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        tabela = Table()
        tabela.add_column("Produto", justify="center")
        tabela.add_row(self.nome)
        tabela.add_row("----------------------")
        tabela.add_row(self.preco)
        print(tabela)




p1 = Produto("Iphone 17 Pro Max", "R$8500")
p2 = Produto("Memória RAM 8GB DDR3", "R$2500")

p1.etiqueta()
p2.etiqueta()


