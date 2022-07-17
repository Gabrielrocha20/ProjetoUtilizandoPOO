from .banco_de_dados import BancoDados


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):

    def logar(self):
        nome = self.nome
        agencia = input('Digite sua agencia: ')
        conta = input('Digite sua conta: ')
        valida = BancoDados(agencia, nome, conta)
        valida.val()
        valida.acessar()
