import shutil
import os

origem = 'Inicio'
destino = 'Inicio/Final'
arquivo = 'teste.txt'

caminho_origem = os.path.join(origem, arquivo)

print(caminho_origem)

caminho_destino = os.path.join(destino, arquivo)

if os.path.exists(caminho_origem):
    shutil.move(caminho_origem, caminho_destino)
    print("Arquivo movido com sucesso para a pasta Final")
elif os.path.exists(caminho_destino):
    shutil.move(caminho_destino, caminho_origem)
    print("Arquivo retornado para a pasta de origem")
else:
    print("Arquivo não encontrado")