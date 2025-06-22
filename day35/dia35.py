def escrever_em_arquivo(arqui, data):
    try:
        with open(arqui, 'w', encoding='utf=8') as file:
            file.write(data)
        print("Dados perfeitamente gravados!!!")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")
        
        
dados = "Aqui estão as informações que serão gravadas em um arquivo, aparti da função criada para facilitar esse processo"
escrever_em_arquivo('saindo.txt', dados)