def divisao(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f'O Resultado é: {resultado}')
    except ZeroDivisionError:
        print("Não é possível dividir por 0")
    except Exception as e:
       print(f"Erro inesperado: {e}") 
       
divisao(10, 2)
divisao(10, 0)