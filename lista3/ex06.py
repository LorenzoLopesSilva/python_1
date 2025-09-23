from traceback import print_tb

usuario = 1234
senha = 9999

usuario_user = int(input("Digite o usuario: "))

if usuario_user == usuario:
    senha_user = int(input("Digite a senha: "))
    if senha_user == senha:
        print("Acesso permitido")
    else:
        print("Senha incorreta")
else:
    print("Usuario invalido")