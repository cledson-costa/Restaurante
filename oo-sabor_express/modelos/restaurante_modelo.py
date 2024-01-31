import os
from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__ (self):
        return f'{self._nome} | {self._categoria} | {self.ativo}'
    
    @property
    def ativo(self):
        return 'V' if self._ativo else 'X'
    
    @classmethod
    def listar_restaurante(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante.ativo}')
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    


os.system('cls')
