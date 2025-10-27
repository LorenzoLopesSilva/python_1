alunos = int(input("Quantos alunos tem na turma? "))
soma = 0

for i in range(alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))

    soma += nota

media = soma/alunos
print(f"A média da turma é: {media:.2f}")