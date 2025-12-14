#Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:

    def __init__ (self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__ (self):
        return f'O nome é {self._nome}, tem {self._idade} anos de idade e é {self._profissao}'
    
    def aniversario (self):
        self._idade += 1

    @property
    def saudacao (self):
        return f'Olá, eu sou {self._nome}, tenho {self._idade} anos e trabalho como {self._profissao}.'
    
pessoa1 = Pessoa('Juan', 28, 'Engenheiro de Dados')
print(pessoa1.saudacao)

#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário
#Crie uma instância da classe e imprima o valor da propriedade titular.

class ContaBancaria:

    def __init__ (self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Nome do titular: {self._titular} | Saldo na consta(R$): {self._saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def titular(self):
        return self._titular

    
pessoa1 = ContaBancaria('Juan', 1500)
pessoa2 = ContaBancaria('Maria', 2500)
print(pessoa1)
print(pessoa2)

ContaBancaria.ativar_conta(pessoa1)
print(pessoa1._ativo)