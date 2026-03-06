from rich import print
from rich.panel import Panel


class Gamer():
    def __init__(self, nome="", nick="", favorito=[]):
        self.nome = nome
        self.nick = nick
        self.favorito = []

    def add_favoritos(self, jogo=""):
        self.favorito.append(jogo)

    def ficha(self):
        jogosformatados = sorted(self.favorito)
        jogos_formatados = "\n".join([f"  [bold yellow]•[/] {jogo}" for jogo in jogosformatados])
        painel = Panel(f"[bold cyan]Nome: [/]{self.nome}\n"
            f"[bold cyan]Nick: [/]{self.nick}\n\n"
            f"[bold cyan]Jogos Favoritos: [/]\n{jogos_formatados}",
                       title=f"[bold magenta]🎮 Ficha do Gamer: {self.nick} 🎮[/]",
            expand=False,
            border_style="green")
        print(painel)

j1 = Gamer()
j1.nome = str(input("Digite seu nome: "))
j1.nick = str(input("Digite seu nickname: "))
j1.add_favoritos("The Legend of Zelda")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.add_favoritos("Pokemón Go")
j1.add_favoritos("Super Mario Odyssey")
j1.ficha()

j2 = Gamer()
j2.nome = str(input("Digite seu nome: "))
j2.nick = str(input("Digite seu nickname: "))
j2.add_favoritos("Super Princess Peach")
j2.add_favoritos("Mineirinho Adventures")
j2.add_favoritos("Roblox")
j2.add_favoritos("Pokopia")
j2.add_favoritos("Super Mario World 2: Yoshi's Island")
j2.ficha()