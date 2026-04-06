from cmath import inf
from idlelib.debugobj_r import remote_object_tree_item

from rich import print
from rich.panel import Panel

# class ControleRemoto(): --> o controle deve ligar, desigar, mudar de canal e aumentar/diminuir o volume
# o @ liga e desliga a TV -> Ela deve começar desligada
# - diminui o volume + aumenta o volume | > avança o canal < volta o canal | 0 sai do programa

# Posso criar 4 variáveis para definir os canais mínimo e máximo e volumes mínimo e máximo -> a fim da manutenção
# do código ficar mais fácil

class ControleRemoto():

    def __init__(self):
        self.estadoInicial = Panel(f"[red]A TV está desligada! [/]", title="TV", style="bold", width=35)
        self.estadoLD = 0
        self.volumeInicial = 1
        self.canalInicial = 1 # Desligado
        print(self.estadoInicial)

    def tela(self):
        return Panel(f"[red]A TV está desligada! [/]", title="TV", style="bold", width=35)

    def controles(self, acao):
        if acao_do_usuario == "@":
            self.variar_ligardesligar()
        if self.estadoLD == 1:
            if acao_do_usuario == "+" or acao_do_usuario == "-":
                self.variar_volume(acao_do_usuario)
            elif acao_do_usuario == ">" or acao_do_usuario == "<":
                self.variar_canal(acao_do_usuario)
        return


    def variar_ligardesligar(self):
        if self.estadoLD:
            self.estadoLD = 0
            print(self.tela())
        else:
            self.estadoLD = 1

#@TODO mudar para somente em uma função trocar canal e mudar volume -> usar match e case

    def variar_volume(self, acao):
        if acao == "+":
            if self.volumeInicial == 5:
                return
            self.volumeInicial += 1
            return
        if self.volumeInicial == 1:
            return
        self.volumeInicial -= 1
        return


    def variar_canal(self, acao):
        if acao == ">":
            if self.canalInicial == 5:
                self.canalInicial = 1
                return
            self.canalInicial += 1
            return
        if self.canalInicial == 1:
            self.canalInicial = 5
            return
        self.canalInicial -= 1
        return

if __name__ == "__main__":
    controleRemoto = ControleRemoto()
    acao_do_usuario = "x"

    while acao_do_usuario != "0":
        acao_do_usuario = str(input(f"< CH{controleRemoto.canalInicial} > - VOL {controleRemoto.volumeInicial} + "))
        controleRemoto.controles(acao_do_usuario)