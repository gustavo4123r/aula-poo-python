class Aluno:
    def __init__(self, nome, treino, matricula):
        self.nome = nome
        self.matricula = matricula
        self.treino = treino    

    def apresentar(self):
        print("Nome:", self.nome)
        print("Matrícula:", self.matricula)
        print("----------")

    def matricular(self, matricula):
        self.matricula = matricula
        print("Aluno matriculado com sucesso.")

    def consultar_treino(self, treino):
        print("Treino:", self.treino)   

aluno1 = Aluno("João", "12345")

aluno1.apresentar()
aluno1.matricular("54321")
aluno1.consultar_treino("Treino A")