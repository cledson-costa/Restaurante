from modelos.restaurante_modelo import Restaurante

restaurante_praca = Restaurante('Peperone','Italiana')
restaurante_mercado = Restaurante('Bevenuto', 'Fast-Food')

def main():
    Restaurante.listar_restaurante()


if __name__ == '__main__':
    main()