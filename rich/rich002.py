from rich import print
from rich.table import Table
from rich import inspect
from rich.traceback import install

install()

def divisao(x, y):
    return x / y


tabela = Table()

tabela.add_column("Nome", style="red", justify="left")
tabela.add_column("Idade", style="blue", justify="center")

tabela.add_row("Francinaldo :coconut:", "35")
tabela.add_row("Ronaldo :tooth:", "50")

print(tabela)


#inspect(int, all=True) -> mostra a documentação de uma forma mais bonita

n1 = float(input("N1: "))
n2 = float(input("N2: "))

print(divisao(n1, n2))