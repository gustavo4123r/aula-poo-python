class Instrutor:
    def __init__(self, nome, aconselhar, salario):
        self.nome = nome
        self.aconselhar = aconselhar
        self.salario = salario

    def apresentar(self):
        print("Nome:", self.nome)
        print("Aconselhar:", self.aconselhar)
        print("Salário:", self.salario)
        print("----------")

    def corrigir(self):
        print("Ta tudo errado ai seu safado, faz direito!")

instrutor1 = Instrutor("Savio", "Treino A", 3000)
instrutor1.apresentar()
instrutor1.corrigir()