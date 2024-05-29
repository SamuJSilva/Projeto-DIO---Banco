from abc import ABC, abstractmethod
import time

class Conta:
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self.numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta (cls, cliente, numero):
        return Conta(cliente, numero)
    
    def sacar(self, valor:float) -> bool:

        if valor > self._saldo:
            print('Valor inválido. Saque não efetuado')
            return False
        
        self._saldo -= valor
        print('Saque efetuado!')
        return True

    def depositar(self, valor:float):
        if valor > 0:
            self._saldo += valor 
            print ('Depósito efetuado com sucesso!')
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3) -> None:
        super().__init__ (numero, cliente)
        self._limite = limite 
        self._limite_saques = limite_saques 

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )
        excedeu_limite = valor > self.limite 
        excedeu_saques = numero_saques > self._limite_saques

        if excedeu_limite:
            print('Você excedeu o valor limite. Operação não realizada')
        elif excedeu_saques:
            print('Você atingiu o limite diário de saques. Operação não realizada')
        else:
            return super().sacar(valor)
        
        return False        

class Historico (Conta):
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,

                "valor": transacao.valor,

                "data": (time.strftime("%a, %d %m(%b) %y, %H : %M", time.localtime())),
            }
        )

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []#list
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome 
        self._data_nascimento = data_nascimento

class Transacao(ABC): # INTERFACE!!!!
    @property
    @abstractmethod
    def valor(self):
        pass
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar (self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque (Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar (self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    escolha = input('''
Digite [1] para DEPÓSITO
Digite [2] para SAQUE
Digite [3] para EXTRATO
Digite [4] para NOVO CLIENTE
Digite [5] para NOVA CONTA
Digite [6] para EXIBIR CONTAS
Digite [7] para SAIR

==> ''')
    return escolha

