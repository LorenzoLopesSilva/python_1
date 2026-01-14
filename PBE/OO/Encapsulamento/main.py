class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def mostrarsaldo(self):
        return self.__saldo
    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo

variavel = ContaBancaria("Lorenzo", 1000.0)

print(variavel.mostrarsaldo())  

print(variavel.depositar(500.0))  