class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0.0
        
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print(f"Valor inválido para depósito")
        
    def sacar(self, valor):
        if valor <= 0:
            print(f"Valor impossível para saque")
        elif valor > self.__saldo:
            print("Saldo inválido.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} feito com sucesso!")
            
    def get_saldo(self):
        return self.__saldo
    
            
bank = Conta("Lara")

bank.depositar(900)
bank.sacar(250)

#Testes de acesso direto ao saldo

try:
    print(bank.__saldo) 
except AttributeError:
    print("Voce nao tem prmissão para acesso direto ao valor do saldo")
    
print(f"O Saldo da sua conta é de R${bank.get_saldo():.2f}")