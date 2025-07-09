class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, e tenho {self.idade} anos.")
    
    
#SubClasses que herdam os atributos de Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
        
    def apresentar(self):
        super().apresentar()
        print(f"Estou matriculado(a), no curso {self.curso}")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        
    def apresentar(self):
        super().apresentar()
        print(f"Eu sou o professor, e vou ministrar a disciplina de {self.disciplina}") 
        
        
        
        
pessoa_comum = Pessoa("Jorginho", 25)
aluno = Aluno ("Nina", 30, "Tecnologia")
prof = Professor("Antonio", 45, "Linguagens de programação") 


pessoa_comum.apresentar()
aluno.apresentar()
prof.apresentar()    