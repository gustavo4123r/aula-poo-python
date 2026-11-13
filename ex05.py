class Cofre:
    def __init__(self, senha):
        self.__senha = senha

    def verificar_senha(self, senha):
            if senha == self.__senha:
                print("Acesso permitido.")
                return True
            else:
                print("Acesso negado.")
                return False

    def alterar_senha(self, senha_atual, nova_senha):
        if senha_atual == self.__senha:
            self.__senha = nova_senha
            print("Senha alterada com sucesso.")
        else:
            print("Senha atual incorreta. Não foi possível alterar a senha.")

cofre = Cofre("1234")
cofre.verificar_senha("1234") 
cofre.alterar_senha("1234", "5678")
cofre.verificar_senha("5678")