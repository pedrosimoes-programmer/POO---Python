from statistics import quantiles

from rich import print
from rich.panel import Panel

# Consumo Padrão: 400g p/ pessoa
# Preço KG: R$82,40/kg

class Churrasco():
    def __init__(self, titulo="Churrasco", pessoas="1"):
        self.pessoas = pessoas
        self.titulo = titulo

    def analisar(self):
        quantidade = self.pessoas * 0.4
        custo_total = quantidade * 82.40
        custo_pessoa = custo_total / quantidade
        painel = Panel(f"Análise do {self.titulo}. Serão necessários {quantidade:.2f}KG de carne. "
                       f"Custo total de R${custo_total:.2f}. Custo por pessoa vai ser de R${custo_pessoa:.2f}.", title=self.titulo, width=35)
        print(painel)




c1 = Churrasco()
c1.titulo = str(input("Digite o nome do churrasco: "))
c1.pessoas = int(input("Digite quantas pessoas são esperadas: "))
c1.analisar()