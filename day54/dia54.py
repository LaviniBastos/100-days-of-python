def adicionar_nota(titulo, conteudo):
    with open("notas.txt", "a") as arquivo:
        arquivo.write(f"{titulo}:\n{conteudo}\n\n")


def visualizar_notas():
    with open("notas.txt", "r") as arquivo:
        notas = arquivo.read().strip()
        print(notas)
        

while True:
    cliente = input("Escolha uma das opções (adicionar/visualizar/sair: ").lower()
    if cliente == "sair":
        print("Encerrando o programa de notas.")
        break
    elif cliente == "adicionar":
        titulo = input("Digite o titulo da nota")
        conteudo = input("Digite o conteudo da nota")
        adicionar_nota(titulo, conteudo)
    elif cliente == "visualizar":
        visualizar_notas()