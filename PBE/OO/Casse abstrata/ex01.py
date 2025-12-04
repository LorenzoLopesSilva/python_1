from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calcular_salario(self):
        return self.salario
    
    def __str__(self):
        return "gerente"

class Vendedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    
    def calcular_salario(self, comissao):
        return self.salario + comissao
    
    def __str__(self):
        return "vendedor"
    
class Estagiario(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calcular_salario(self):
        return self.salario - self.salario * 0.2
    
    def __str__(self):
        return "estagiario"


gerente = Gerente("Lorenzo", 10000)
vendedor = Vendedor("Maria", 5000)
estagiario = Estagiario("Pedro", 2000)

funcionarios = [gerente, vendedor, estagiario]

for funcionario in funcionarios:
    if isinstance(funcionario, Vendedor):
        print(funcionario.calcular_salario(1000))
    else:
        print(funcionario.calcular_salario())






