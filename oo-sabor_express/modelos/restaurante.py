class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmer')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

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

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

#Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(restaurante_pizza.categoria)

#Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

#Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'O nome do restaurante é {restaurante_pizza.nome}, a categoria é {restaurante_pizza.categoria}')

