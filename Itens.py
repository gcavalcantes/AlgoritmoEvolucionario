'''
Lista de itens.
'''
import random


class Itens():
    '''
        Classe responsável por lidar com as características dos itens e geração de itens
        '''
    codigo = []
    # TODO Variável que recebe o número de itens a serem criados

    # Método init
    def __init__(self, existe, peso, beneficio):
        '''
        Construto de OOP que cria um objeto quando a classe é chamada
                e é passado como o primeiro parâmetro deste método.
        '''
        self.item = [[],
                     [8, 10, 4, 6, 12, 14, 7, 5],
                     [10, 14, 8, 9, 16, 17, 9, 9]]
        self.existe = existe
        self.peso = peso
        self.beneficio = beneficio

    def gerarItens():
        '''
        Função responsável por criar lista de itens que são
        '''
        itensExistentes = GerarItensExistentes()

    def gerarItensExistentes(quantidade):
        '''
        Decide quais os itens que estão disponíveis na lista
        '''
        contador = 0
        while contador <= 7:
            num = random.randint(0, 1)
            self.item[[contador], [0], [0]] = num
            contador = contador + 1
        return self.item
