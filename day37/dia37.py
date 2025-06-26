def calculo_media_arquivo(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            numeros = []
            for linha in file:
                linha = linha.strip()
                if linha:
                    numeros.append(float(linha))
                    
        if numeros:
            media = sum(numeros) / len(numeros)
            print(f"A Média dos números contidos no arquivo é: {media}")
        else:
            print("O arquivo está vazio, ou não contém números")
            
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except ValueError:
        print('O arquivo contém valores que não são números')
    except Exception as e:
        print(f'Erro inesperado: {e}')
        
        
calculo_media_arquivo('numeros.txt')