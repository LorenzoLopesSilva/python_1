class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def total_alunos(self):
        print(f"Total de alunos no curso {self.nome}: {len(self.alunos)}")
    
    def listar_alunos(self):
        print(f"Alunos no curso {self.nome}:")
        for aluno in self.alunos:
            print(f"{aluno}")

curso1 = Curso("Matemática")
curso1.adicionar_aluno("Lorenzo")
curso1.adicionar_aluno("Ingrid")
curso1.adicionar_aluno("Rafa")

curso1.total_alunos()
curso1.listar_alunos()