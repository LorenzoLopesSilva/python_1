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
            print("\nEmpréstimo realizado com sucesso.")
        else:
            print("Desculpe, este livro não está disponível no momento.")
    
    def devolver(self):
        if self.__quantidade_disponivel < self.__quantidade_total:
            self.__quantidade_disponivel += 1
            print("\nDevolução realizada com sucesso.")
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
    
    def cadastrar_livro(self, livro: Livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' cadastrado com sucesso.")
    
    def cadastrar_usuario(self, usuario: Usuario):
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
                            usuario.limite_emprestimo -= 1
                            print(emprestimo)
                            return emprestimo
                else:
                    print("\nLimite de empréstimos atingido")
                    return False
                    
        print("\nLivro ou usuário incorretos")
                
    
    def devolver_livro(self, usuario_id, isbm):
        if len(self.emprestimos) > 0:
            for emprestimo in self.emprestimos:
                if emprestimo.usuario.id == usuario_id and emprestimo.livro.ISBM == isbm:
                    emprestimo.livro.devolver()
                    self.emprestimos.remove(emprestimo)
                    return True
                
            print("Emprestimo não encontrado")
        else:
            print("Nenhum empréstimo encontrado")
    
    def listar_emprestimos_ativos(self):
        lista_emprestimos = []
        for emprestimo in self.emprestimos:
            lista_emprestimos.append(f"{emprestimo.livro.titulo} emprestado para {emprestimo.usuario.nome} em {emprestimo.data_emprestimo}")
            print(emprestimo)
        return lista_emprestimos


livro1 = Livro("1984", "George Orwell", 1949, 1111, 5, 5)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1899, 2222, 3, 3)
livro3 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 3333, 2, 2)

aluno1 = Aluno("Lorenzo", 1, "senha123")
professor1 = Professor("Maria", 2, "senha456")

print(aluno1.id)
print(livro1.ISBM)
biblioteca = Biblioteca()

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)
biblioteca.cadastrar_livro(livro3)

biblioteca.cadastrar_usuario(aluno1)
biblioteca.cadastrar_usuario(professor1)

biblioteca.emprestar_livro(aluno1.id, livro1.ISBM, "10/09/2023")
biblioteca.emprestar_livro(aluno1.id, livro2.ISBM, "11/09/2023")
biblioteca.emprestar_livro(aluno1.id, livro3.ISBM, "12/09/2023")

biblioteca.emprestar_livro(aluno1.id, livro1.ISBM, "13/09/2023")
biblioteca.emprestar_livro(aluno1.id, livro2.ISBM, "14/09/2023")

biblioteca.emprestar_livro(professor1.id, livro1.ISBM, "15/09/2023")

biblioteca.emprestar_livro(professor1.id, 123124, "16/09/2023")

biblioteca.devolver_livro(professor1.id, livro1.ISBM)
print("")
biblioteca.listar_emprestimos_ativos()






