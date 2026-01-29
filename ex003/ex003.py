# Criando uma conta bancária

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos

    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Seu saldo é R${self.saldo:.2f}.")

    def __str__(self):
        return  f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo"

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente. Saque de R${valor:.2f} NÃO autorizado.")
        else:
            print(f"O saque de R${valor:.2f} foi autorizado")
            self.saldo -= valor

    def depositar(self, valor):
        print(f"O depósito de R${valor:.2f} foi autorizado")
        self.saldo += valor



c1 = ContaBancaria(43651, "Pedro", 3050)

c = int(input("Sacar [1] ou Depositar [2]: "))

if c == 1:
    valor = int(input("Quanto você quer sacar: "))
    c1.sacar(valor)
elif c == 2:
    valor = int(input("Quanto você quer depositar: "))
    c1.depositar(valor)
else:
    print("Você digitou outro número. Tente novamente.")

print(c1)