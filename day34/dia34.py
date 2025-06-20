
def ler_arquivo(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            conteudo = file.read()
            print(conteudo)
    except FileNotFoundError:
        print('Arquivo não foi encontrado.')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')
        
        
ler_arquivo('teste.txt')

