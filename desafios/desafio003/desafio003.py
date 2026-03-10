from rich import print
import time

class Livro():
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1

        print(f":book: Você abriu o livro [red]{self.titulo}[/] que contém [blue]{self.paginas} páginas[/]. Você está na [yellow]página {self.pagina_atual}[/].\n")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end="")
                time.sleep(0.2)
                cont += 1
        print(f"Você avançou {cont} página(s), e agora está na página {self.pagina_atual}.")
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro {self.titulo}[/red]")

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.paginas else False

l1 = Livro("Empreendedores Inteligentes Enriquecem", 20)

l1.avancar_paginas(10)
l1.avancar_paginas(27)
l1.avancar_paginas(10)