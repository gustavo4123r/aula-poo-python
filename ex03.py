class Animal:
    def __init__(self, nome):
        self.nome = nome 

    def apresentar(self):
        print("Meu nome é:", self.nome)

class Cachorro(Animal):
    def latir(self):
        print("Au Au!")
class Gato(Animal):
    def miar(self):
        print("Miau!")

cachorro = Cachorro("Dorota")
gato = Gato("Maria Belém")

cachorro.apresentar()
cachorro.latir()

gato.apresentar()
gato.miar()