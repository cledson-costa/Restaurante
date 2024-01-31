from modelos.restaurante_modelo import Restaurante
from modelos.avaliacao import Avaliacao

restaurante_praca = Restaurante('Peperone','Italiana')
restaurante_mercado = Restaurante('Bevenuto', 'Fast-Food')
nota1 = Avaliacao('Cledson', 10)
nota2 = Avaliacao('Cledson', 8)
nota3 = Avaliacao('Cledson', 4)


def main():
    Restaurante.listar_restaurante()


if __name__ == '__main__':
    main()