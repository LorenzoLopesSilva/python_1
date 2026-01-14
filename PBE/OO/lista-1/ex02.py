class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.lido = False
    
    def marcar_como_lido(self):
        self.lido = True
    
    def resumo (self):
        if self.lido:
            status = "Lido"
        else:
            status = "Não lido"
        
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\nStatus: {status}")

livro1 = Livro("Percy Jacson e os Olimpianos", "Rick Riordan", 377)
livro1.marcar_como_lido()
livro1.resumo()

livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1216)
livro2.resumo()