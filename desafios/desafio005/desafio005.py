from rich import print

class Caneta():
    def __init__(self, cor=""):
        self.cor = cor
        self.tampada = True

    def quebrar_linha(self, linhas=1):
        c = 0
        for cont in range(0, linhas, 1):
            print()
            c += 1

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        cores_validas = {
            "verde": "green",
            "azul": "blue",
            "vermelho": "red"
        }

        cor_formatada = self.cor.strip().lower()

        if self.tampada:
            print(f"Não é possível escrever. A [{cores_validas[cor_formatada]}]caneta[/] está tampada!")
            return
        if cor_formatada in cores_validas:
            cor_rich = cores_validas[cor_formatada]
            print(f"[{cor_rich}]{texto}[/]")
        else:
            print(f"\n[yellow]Cor '{self.cor}' indisponível. Use Verde, Azul ou Vermelho.[/]")


c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?!")
c1.quebrar_linha(1)
c2.escrever("Agora tudo está comunista!")
c1.quebrar_linha(2)
c3.escrever("Agora tudo está alviverde imponente!")

c3.tampar()

c3.escrever("Vamos à praia.")
