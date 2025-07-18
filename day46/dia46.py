class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
        
    def exibir_informacoes(self):
        print(f"O titulo do livro é: {self.titulo}")
        print(f"Autor: {self.autor}")
        
        
livro = Livro("Pai Rico, pai pobre", "Robert Kiyosaki")
livro.exibir_informacoes()