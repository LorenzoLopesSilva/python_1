from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Quadradado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4

quadrado = Quadradado(5)
print(quadrado.area())
print(quadrado.perimetro())