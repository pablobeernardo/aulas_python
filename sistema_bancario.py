from abc import ABC, abstractclassmethod, abstractproperty
import datetime


class Cliente:
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf      

class Conta:     
    def __init__(self, saldo, numero, cliente):
        self.saldo = saldo
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property  
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Saldo insuficiente')

        elif valor > 0:
            self.saldo = saldo - valor
            print('Saque realizado com sucesso')
            return True
        
        else:
            print('Valor invalido')

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print('Deposito realizado com sucesso')
        
        else:
            print('Valor invalido')
            return False
    
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if 
             transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('Valor de saque maior que o limite')

        elif excedeu_saques:
            print('Limite de saques atingido')

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'Agência: {self.agencia} - Conta: {self.numero} - Titular: {self.cliente.nome}'

class Historico:
    def __init__(self):
        self.transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
        
    




    

    
    
        