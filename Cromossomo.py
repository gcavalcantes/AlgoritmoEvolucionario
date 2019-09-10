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
            if random.random() >= .5:
                # Valor do gene é 1
                novo_valor += '1'
            else:
                # Caso contrário o valor de gene é 0
                novo_valor += '0'
        self.alterar_valor(novo_valor)
                
    # Método de crossover que recebe dois cromossomos
    def crossover(self, aux_cromossomo):
        # Divide o cromossomo aleatoriamente
        corta_index = int(random.random() * int(self.tamanho))
        novo_valor = ""
        if random.random() > .5:
            novo_valor = self.valor[0:corta_index] + aux_cromossomo.valor[corta_index:len(aux_cromossomo.valor)]
        else:
            novo_valor = aux_cromossomo.valor[0:corta_index] + self.valor[corta_index:len(aux_cromossomo.valor)]
        cromossomo_filho = Cromossomo(novo_valor)
        cromossomo_filho.alterar_valor(novo_valor)
        return cromossomo_filho
    
    # Método de mutação dos genes
    def mutacao(self,perc_mutacao):
        comeco, aux, fim = ['','','']
        # Para cada caractere em um cromossomo
        for i in range(len(self.tamanho)):
            # Se um número aleatório for menor que o percentual de mutação
            if random.random() < perc_mutacao:
                # A cada iteração as variáveis recebem uma troca de valor de acordo com 'i', ou não
                comeco = self.valor[0:i]
                fim = self.valor[i+1:int(self.tamanho)]
                aux = self.valor[i]
                # Se a variável aux for igual a 1
                if aux == '1':
                    aux = '0'
                else:
                    aux ='1'
                # Variável valor recebe a nova mistura representando a mutação.
                self.alterar_valor(comeco+aux+fim)

    # Método para valores reais
    def v_real(self, i = 0, s = 100):
        return i + (s - i)/(2 ** self.tamanho -1) * int(self.valor, 2)

    # Método para avaliar código binário
    def avaliar(self):
        x = int(self.valor, 2)
        # Fórmula de avaliação seno(x²)/(3 - cos(e) - x)
        self.avaliacao = math.sin(x**2)/(3-math.cos(math.e) - x)
        return self.avaliacao

    # Método para representar o indivíduo como String
    def __repr__(self):
        return "Código binário:[%s] | Avaliacao[%.2f] | Nível de facilidade[%d]" % (self.valor, self.avaliacao, int(self.valor, 2))