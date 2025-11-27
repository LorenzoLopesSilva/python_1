class Livro:
    def __init__(self, titulo, autor, ano, ISBM, quantidade_total, quantidade_disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.ISBM = ISBM
        self.__quantidade_total = quantidade_total
        self.__quantidade_disponivel = quantidade_disponivel
    
    def emprestar(self):
        if self.__quantidade_disponivel > 0:
            self.__quantidade_disponivel -= 1
            print("Empréstimo realizado com sucesso.")
        else:
            print("Desculpe, este livro não está disponível no momento.")
    
    def devolver(self):
        if self.__quantidade_disponivel < self.__quantidade_total:
            self.__quantidade_disponivel += 1
            print("Devolução realizada com sucesso.")
        else:
            print("Todas as cópias já estão na biblioteca.")
    
    def __str__(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Ano: {self.ano} | ISBM: {self.ISBM} | Quanridade Total: {self.__quantidade_total} | Quantidade Disponível: {self.__quantidade_disponivel}"

class Usuario:
    def __init__(self, nome, id, senha):
        self.nome = nome
        self.id = id
        self.__senha = senha
    
    def poder_emprestar(self, limite):
        if limite > 0:
            return True
        else:
            return False
    
    def __str__(self):
        return f"Usuário: {self.nome}"

class Aluno(Usuario):
    def __init__(self, nome, id, senha):
        super().__init__(nome, id, senha)
        self.limite_emprestimo = 3

    def poder_emprestar(self):
        return super().poder_emprestar(self.limite_emprestimo)

class Professor(Usuario):
    def __init__(self, nome, id, senha):
        super().__init__(nome, id, senha)
        self.limite_emprestimo = 5

    def poder_emprestar(self):
        return super().poder_emprestar(self.limite_emprestimo)

class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
    
    def marcar_devolucao(self, data_devolucao):
        self.data_devolucao = data_devolucao
        print("Devolução marcada para:", self.data_devolucao)
    
    def __str__(self):
        return f"Empréstimo: {self.livro.titulo} para {self.usuario.nome} em {self.data_emprestimo}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []
    
    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' cadastrado com sucesso.")
    
    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado com sucesso.")
    
    def buscar_livro_por_titulo(self, titulo): 
        for livro in self.livros:
           if livro.titulo == titulo:
               return livro
        return "Livro não encontrado."
    
    def emprestar_livro(self, usuario_id, isbm, data):
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                if usuario.poder_emprestar():
                    for livro in self.livros:
                        if livro.ISBM == isbm:
                            emprestimo = Emprestimo(usuario, livro, data)
                            self.emprestimos.append(emprestimo)
                            livro.emprestar()
                            print(emprestimo)
                        else:
                            print("Livro não encontrado")
                else:
                    print("Limite de empréstimos atingido")
            else:
                print("Usuário não encontrado") 
    
    def devolver_livro(self, usuario_id, isbm):
        for emprestimo in self.emprestimos:
            if emprestimo.usuario.id == usuario_id and emprestimo.livro.ISBM == isbm:
                emprestimo.livro.devolver()
                self.emprestimos.remove(emprestimo)
            else:
                print("Emprestimo não encontrado")
    
    def listar_emprestimos_ativos(self):
        lista_emprestimos = []
        for emprestimo in self.emprestimos:
            lista_emprestimos.append(f"{emprestimo.livro.titulo} emprestado para {emprestimo.usuario.nome} em {emprestimo.data_emprestimo}")
        return lista_emprestimos


livro1 = Livro("1984", "George Orwell", 1949, "1234567890", 5, 5)

aluno1 = Aluno("Ana", "A001", "senha123")

biblioteca = Biblioteca()
biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_usuario(aluno1)
biblioteca.emprestar_livro("A001", "1234567890", "01/10/2024")
print(biblioteca.buscar_livro_por_titulo(livro1.titulo))

print(biblioteca.listar_emprestimos_ativos())

biblioteca.devolver_livro("A001", "1234567890")

print(biblioteca.buscar_livro_por_titulo(livro1.titulo))

