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
        
    # Método de atualização de valor do genes de um cromossomo
    def alterar_valor(self, novo_valor):
        self.valor = novo_valor
        
    # Método de inicialização da geração de números para o cromossomo
    def inicia(self):
        # Variável para receber o novo gene
        novo_valor = ""
        # Para cada número no cromossomo
        for i in range(self.tamanho):
            # Se um número real for maior que 0,5
            if random.random() > .5:
                # Valor do gene é 1
                novo_valor += '1'
            else:
                # Caso contrário o valor de gene é 0
                novo_valor += '0'
        self.alterar_valor(novo_valor)
                
    # TODO Método de crossover que recebe dois cromossomos
    def crossover(self, aux_cromossomo):
        # Divide o cromossomo aleatoriamente
        corta_index = int(random.random() * self.tamanho)
        novo_valor = ""
        if random.random() > .5:
            novo_valor = self.valor[0:corta_index] + aux_cromossomo


    # TODO Método de mutação dos genes

    # TODO Método para valores reais

    # TODO Método para avaliar cromossomo

    # TODO Método para representar o indivíduo como String