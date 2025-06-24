def adicionar_ao_arquivo(arquivo, data):
    try:
        with open(arquivo, 'a', encoding='utf-8') as file:
            file.write(data + '\n')
        print("Dados adicionados com sucesso!!")
    except Exception as e:
        print(f" Erro ao adicionar dados ao arquivo: {e}")
        
        
        
conteudo_novo = "Essa linha será adicionada ao ultima linha do arquivo"
adicionar_ao_arquivo('saindo.txt', conteudo_novo)
