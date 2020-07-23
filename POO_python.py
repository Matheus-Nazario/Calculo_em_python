/



class livro:  #classe livro
    def __ini__(self): #sempre vai ter SELF no programa #doi _ antes e depois
        self.titulo = None  #pertence a primeira class. acessar o atributo dentro da minha classe
        self.autor = None #atributo autor, título, preco
        self.preco = None

    def exibir_dados(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Preço:", self.preco)

meu_livro = livro()
meu_livro.titulo = "aaaaaaaaaa"
meu_livro.autor = "bbbbbb"
meu_livro.preco= 20.00

meu_livro.exibir_dados()