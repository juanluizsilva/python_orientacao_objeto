from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmer')
restaurante_praca.receber_avalicao('Juan', 10)
restaurante_praca.receber_avalicao('Maria', 9.5)
restaurante_praca.receber_avalicao('Frida', 2)
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

# restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()