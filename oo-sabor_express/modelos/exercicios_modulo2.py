#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:

    lista_carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.lista_carros.append(self)

    def __str__(self):
        return f'Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano}'
    
    def exibe_carros():
        for veiculo in Carro.lista_carros:
            print(veiculo)

Carro1 = Carro('Onix', 'Preto', 2016)
Carro2 = Carro('Tracker', 'Branco', 2020)
Carro3 = Carro('IX35', 'Prata', 2016)

Carro.exibe_carros()

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'

Restaurante1 = Restaurante('Villa', 'Brasileira')
print(Restaurante1)