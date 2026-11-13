class Gerente_de_academia:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def apresentar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Salário:", self.salario)
        print("----------")

    def mandar(self):
        print("Estamos contratando novos funcionários para a academia.")

gerente1 = Gerente_de_academia("Carlos", 35, 5000)
gerente1.apresentar()
gerente1.mandar()