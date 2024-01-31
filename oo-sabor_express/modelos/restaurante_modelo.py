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
            print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante.ativo}' | str(restaurante.media_avaliacao))
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quant_notas = len(self._avaliacao)
        media = round(soma_notas/quant_notas, 1)
        return media


os.system('cls')
