# Definindo uma exceção personalizada
class ValorNegativoError(Exception):
    def __init__(self, valor):
        super().__init__(f"Valor inválido: {valor}. Não são permitidos números negativos.")


def verificar_valor(valor):
    if valor < 0:
        raise ValorNegativoError(valor)
    print(f"✅ Valor aceito: {valor}")


try:
    verificar_valor(10)
    verificar_valor(-5)
except ValorNegativoError as e:
    print(e)