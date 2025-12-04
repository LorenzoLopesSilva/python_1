class Pessoas:
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato

class Salas:
    def __init__(self, codigo, capacidade, localizacao):
        self.codigo = codigo
        self.capacidade = capacidade
        self.localizacao = localizacao

class Reservas:
    def __init__(self, pessoa: Pessoas, sala: Salas, inicio, fim):
        self.pessoa = pessoa
        self.sala = sala
        self.inicio = inicio
        self.fim = fim

reservas = []
pessoa1 = Pessoas("Lorenzo", 123456789)
pessoa2 = Pessoas("Lucas", 987654321)

sala1 = Salas(501, 32, "Senai")
sala2 = Salas(502, 32, "Senai")

reserva1 = Reservas(pessoa1, sala1, "10:00", "12:00")
reserva2 = Reservas(pessoa2, sala2, "12:00", "14:00")
reserva3 = Reservas(pessoa2, sala1, "10:00", '12:00')

reservas.append(reserva1)
reservas.append(reserva2)
reservas.append(reserva3)


    