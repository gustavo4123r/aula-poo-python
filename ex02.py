class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def consultar_saldo(self):
        print("Saldo:", self._saldo)

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado!")

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")


conta = ContaBancaria("João", 500)

conta.consultar_saldo()
conta.depositar(200)
conta.sacar(100)
conta.consultar_saldo()