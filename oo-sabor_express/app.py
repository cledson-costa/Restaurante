from modelos.restaurante_modelo import Restaurante
from modelos.avaliacao import Avaliacao


restaurante_praca = Restaurante('Peperone','Italiana')
restaurante_mercado = Restaurante('Bevenuto', 'Fast-Food')
restaurante_mercado.receber_avaliacao('Cledson', 10)
restaurante_mercado.receber_avaliacao('Miguel', 8)
restaurante_mercado.receber_avaliacao('Teresa', 4)
restaurante_praca.receber_avaliacao('Vanessa', 9)
restaurante_praca.receber_avaliacao('Yasmin', 4)
restaurante_praca.receber_avaliacao('Carol', 4)



def main():
    Restaurante.listar_restaurante()


if __name__ == '__main__':
    main()