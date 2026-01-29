# Declaração de Classe

class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade!"


# Declaração de Objetos

g1 = Gafanhoto()

g1.nome = str(input("Digite seu nome: "))
g1.idade = int(input("Digite sua idade: "))

g1.aniversario()

print(g1.mensagem())