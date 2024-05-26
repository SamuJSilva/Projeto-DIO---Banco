from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico) -> None:
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = Cliente
        self._historico = Historico
    
    def saldo(self) ->float:
        pass

    @classmethod
    def nova_conta(cls,saldo, agencia, cliente, numero, historico):
        pass
        return Conta(saldo, agencia, cliente, numero, historico)
    
    def sacar(self, valor:float) -> bool:
        pass

    def depositar(self, valor:float):
        pass



class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite #float
        self._limite_saques = limite_saques #int

class Historico (Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)

    def adicionar_transacao(self, transacao):
        pass

class Cliente (Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, endereco, contas) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._endereco = endereco
        self._contas = contas #list
    
    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(conta):
        pass

class PessoaFisica(Cliente):
    def __init__(self, saldo, numero, agencia, cliente, historico, endereco, contas, cpf, nome, data_nascimento) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico, endereco, contas)
        self._cpf = cpf
        self._nome = nome 
        self._data_nascimento = data_nascimento

class Transacao(Historico): # INTERFACE!!!!
    def __init__(self, saldo, numero, agencia, cliente, historico) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, saldo, numero, agencia, cliente, historico, valor) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._valor = valor
    
    def registrar(self, conta):
        pass

class Saque (Transacao):
    def __init__(self, saldo, numero, agencia, cliente, historico, valor) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._valor = valor

    def registrar(self, conta):
        pass
