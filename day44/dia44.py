class ContaDoBanco:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0
        
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")
            
            
    def sacar(self,valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque")
            
        elif valor <= 0:
            print("Valor de saque inválido.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            
            
    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular} é de: R${self.saldo:.2f}")
        
conta = ContaDoBanco("Joel")
conta.consultar_saldo()
conta.depositar(5000)
conta.sacar(2030)
conta.consultar_saldo()
conta.sacar(10000)