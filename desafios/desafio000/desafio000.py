from rich import print


class Funcionario():
    def __init__(self, nome="", setor="", cargo=""):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        print(f":hand: Olá! Meu nome é [blue]{self.nome}[/], sou {self.cargo} do setor de {self.setor}.")

    #def __str__(self):
        #return f":hand: Olá! Meu nome é [blue]{self.nome}[/], sou {self.cargo} do setor de {self.setor}."


c1 = Funcionario()

c1.nome = str(input("Digite seu nome: "))
c1.setor = str(input("Digite seu setor: "))
c1.cargo = str(input("Digite seu cargo: "))

print(c1.apresentacao())

c2 = Funcionario("Pedro", "Financeiro", "Analista")
print((c2.apresentacao()))