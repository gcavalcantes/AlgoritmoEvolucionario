'''
Classe cromossomo

Esta classe contém todas as características e métodos referentes a um indivíduo da população.

'''

import math, random

# TODO Classe dos cromossomos
class Cromossomo():

    # Método __init__: contém as características de um cromossomo
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.valor = ""
        self.avaliacao = -1
        
    # TODO Método de atualização de valor do genes de um cromossomo
    def alterar_valor(self, novo_valor):
        self.valor = novo_valor
        
    # TODO Método de inicialização
    def inicia(self):

    # TODO Método de crossover

    # TODO Método de mutação dos genes

    # TODO Método para valores reais

    # TODO Método para avaliar cromossomo

    # TODO Método para representar o indivíduo como String