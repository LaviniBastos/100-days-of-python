class excecaoparavalorNegativo(Exception):
    def __init__(self, valor):
        super().__init__(f"Valor negativo não é permitido: {valor}")
        
        
        
def verifica_numero(numero):
    if numero < 0:
        raise excecaoparavalorNegativo(numero)
    print(f"Esse valor é válido: {numero}")
    
    
try:
    verifica_numero(100)
    verifica_numero(-2)
except excecaoparavalorNegativo as e:
    print(e)
    