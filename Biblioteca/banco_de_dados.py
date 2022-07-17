from .Conta import ContaPoupanca, ContaCorrente

class BancoDados:

    def __init__(self, agencia, cliente, conta, ):
        self.agencia = agencia
        self.cliente = cliente
        self.conta = conta
        self._aceito = 0

    @property
    def aceito(self):
        return self._aceito

    def val(self):
        bdd = (['1001', 'Gabriel', '122122'],
               ['1002', 'Milena', '233233'],
               ['1001', 'Luiz', '344344'],
               ['1002', 'Otavio', '455455'])
        log = []

        for valida in bdd:
            if self.agencia in valida[0] and self.cliente in valida[1] and self.conta in valida[2]:
                self._aceito = 1
                log = valida
                break
            self._aceito = 0
        if self._aceito == 1:
            print('valido')

    def acessar(self):
        if self._aceito == 1:
            if self.agencia == '1001':
                cp = ContaPoupanca(self.agencia, self.conta, 0)
                deposita_1 = int(input('Bem vindo ao Banco faça seu primeiro deposito..DIGITE O VALOR: '))
                cp.depositar(deposita_1)
                while True:
                    depo_sac = input(' "Depositar"[1] , "Sacar"[2] ou "Sair"[3] Digite [1/2/3]: ')
                    if depo_sac == '1':
                        deposita = int(input('Digite um valor para fazer o deposito: '))
                        print()
                        print()
                        cp.depositar(deposita)
                        pass
                    elif depo_sac == '2':
                        saca = int(input('Digite um valor para fazer o saque: '))
                        print()
                        print()
                        cp.sacar(saca)
                        pass
                    else:
                        print('Ate a Proxima')
                        return
            elif self.agencia == '1002':
                cc = ContaCorrente(self.agencia, self.conta, 0)
                deposita_1 = int(input('Bem vindo ao Banco faça seu primeiro deposito VALOR: '))
                cc.depositar(deposita_1)
                while True:
                    depo_sac = input('"Depositar"[1] , "Sacar"[2] ou "Sair"[3] Digite [1/2/3] : ')
                    if depo_sac == '1':
                        deposita = int(input('Digite um valor para fazer o deposito: '))
                        print()
                        print()
                        cc.depositar(deposita)
                        pass
                    elif depo_sac == '2':
                        saca = int(input('Digite um valor para fazer o saque: '))
                        print()
                        print()
                        cc.sacar(saca)
                        pass
                    else:
                        print('Ate a Proxima')
                        return
        else:
            print('Acesso Invalido')
