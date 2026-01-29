# Declaração de Classe

class Gafanhoto:
    def __init__(self, nome = "vazio", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade!"


# Declaração de Objetos

g1 = Gafanhoto("Maria", 34)
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto("MrBeast", 29)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())
