def erro_arqui(arq):
    try:
        with open(arq, 'r', encoding='utf-8') as file:
            conteudo = file.read()
            print(conteudo)
            
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as e:
        print(f"Erro inesperado ocorreu: {e}")
        
        
erro_arqui('arquivinho.txt')