class Restaurante:
    nome = ''
    categoria = '' 
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

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

