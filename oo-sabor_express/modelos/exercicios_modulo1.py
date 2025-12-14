class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    def listar_restaurantes():
        print (f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

restaurante_praca = Restaurante('praça', 'Gourmer')
restaurante_praca.nome = 'Praça 2.0'
restaurante_pizza = Restaurante('pizza Express', 'Italiana')

Restaurante.listar_restaurantes()


print(restaurante_praca)
print(restaurante_pizza)

if restaurante_praca.ativo == True:
    print ('O restaurante esta ativo')
else:
    print ('O restaurante não esta ativo')

categoria = restaurante_praca.categoria
print(categoria)

#Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.categoria = 'Bistrô'

#Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()

restaurante_pizza._nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

#Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(restaurante_pizza.categoria)

#Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

#Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'O nome do restaurante é {restaurante_pizza._nome}, a categoria é {restaurante_pizza.categoria}')