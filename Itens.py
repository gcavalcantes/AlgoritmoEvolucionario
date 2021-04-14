'''
Lista de itens.
'''
import random
import Principal
import ProblemaMochila


class Itens():
    '''
        Classe responsável por lidar com as características dos itens e geração de itens
        '''
    codigo = []
    # TODO Variável que recebe o número de itens a serem criados
    numItens = Principal.pergunta1

    # Método init
    def __init__(self, existe, peso, beneficio):
        '''
        Construto de OOP que cria um objeto quando a classe é chamada
                e é passado como o primeiro parâmetro deste método.
        '''
        self.item = [[]]
        self.existe = existe
        self.peso = peso
        self.beneficio = beneficio

    def gerarItens(self):
        '''
        Função responsável por criar lista de itens que são
        '''
        itensExistentes = gerarItensNaLista()

    def gerarItensNaLista(self, quantidade):
        '''
        Decide quais os itens que estão disponíveis na lista
        '''
        contador = 0
        while contador <= 7:
            num = random.randint(0, 1)
            self.item[[contador], [0], [0]] = num
            contador = contador + 1
        return self.item
