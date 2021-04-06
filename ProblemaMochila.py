'''
Problema da mochila.

Código por Gabriel Cavalcante
'''


class Mochila():
    '''
    Classe para as características e funções da mochila
    '''

    def _init_(self, listaDeObjetos, pesoTotal, quantidadeItens):
        '''
        Construto de OOP que cria um objeto quando a classe é chamada
        e é passado como o primeiro parâmetro deste método.
        '''

        # Lista por código
        self.listaDeObjetos = []
        self.pesoTotal = 0
        self.quantidadeItens = 0

    def inserirNaMochila(self, codigo):
        """
        Insere um objeto na mochila.
        """
        for x in self.listaDeObjetos:
            listaDeObjetos = []
