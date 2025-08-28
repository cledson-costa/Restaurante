from modelos.restaurante_modelo import Restaurante
from modelos.avaliacao import Avaliacao


restaurante_praca = Restaurante('Peperone','Italiana')
restaurante_mercado = Restaurante('Bevenuto', 'Fast-Food')
restaurante_mercado.receber_avaliacao('Cledson', 10)
restaurante_mercado.receber_avaliacao('Luiz', 8)
restaurante_mercado.receber_avaliacao('Maria', 4)
restaurante_praca.receber_avaliacao('Raquel', 9)
restaurante_praca.receber_avaliacao('Marta', 4)
restaurante_praca.receber_avaliacao('Carolina', 4)



def main():
    Restaurante.listar_restaurante()


if __name__ == '__main__':
    main()
