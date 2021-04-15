'''
Arquivo responsável por reunir todos os outros para o algoritmo genético.
'''

import ProblemaMochila
import Itens


class Principal():
    '''
    Classe principal do programa.
    '''

    def __init__(self):
        # Variável para o número de itens na solução
        self.pergunta1 = 0
        # Variável para o valor dos itens na pergunta 2. Deve ser int.
        self.pergunta2Valor = []
        # Variável para o peso do item na pergunta 2. Deve ser float.
        self.pergunta3Peso = []
        # Variável para a quantidade de peso que a mochila pode suportar.
        self.pergunta4Tamanho = 0

        super().__init__()

    # Função para a pergunta 1
    def pergunta_1(self):
        """
        Função que retorna o número de itens que será usado na solução e também pelos outros métodos da classe.
        """

        try:
            self.pergunta1 = int(input(
                print("Quantos itens terá a lista? (Número inteiro)")))
            while (self.pergunta1 < 2):
                print("Valor dever ser maior que um.")
                self.pergunta1 = int(input(
                    print("Quantos itens terá a lista? (Número inteiro) ")))
        except ValueError:
            print('Erro: Resposta precisa ser um número inteiro.')

        return self.pergunta1

    # Função para a pergunta 2
    def pergunta_2(self, numItens):
        """
        Retorna o valor do item
        contador: conta até o número de itens na lista.
        """

        contador = 1
        try:
            # Loop para a segunda pergunta.
            while contador <= numItens:
                self.pergunta2Valor = int(input(
                    print('Qual o valor do item {}?'.format(contador))))
                contador += 1
        # Tratamento de erro para caso a pergunta não seja um inteiro.
        except ValueError as ve:
            print('Erro: Resposta precisa ser um número inteiro.')

    # Função para a pergunta 2
    def pergunta_3(self, numItens):
        """
        Retorna o peso do item
        contador: conta até o número de itens na lista.
        """
        contador = 1
        try:
            # Loop para a segunda pergunta.
            while contador <= numItens:
                self.pergunta3Peso = float(
                    input(print('Qual o peso do item {}?'.format(contador))))
                contador += 1
        # Tratamento de erro para caso a pergunta não seja um inteiro.
        except ValueError as ve:
            print('Erro: Resposta precisa ser um número inteiro.')
        return self.pergunta3Peso

    # Função para a pergunta 3
    def pergunta_4(self):
        """
        Função responsável por definir o tamanho da mochila
        """
        # Definindo o tamanho da mochila
        try:
            self.pergunta4Tamanho = int(
                input(print('Qual o espaço da mochila? (número inteiro)'.format())))
        except ValueError as ve:
            print('Erro: Resposta precisa ser um número inteiro.')

        return self.pergunta4Tamanho

    # TODO Função para fazer as perguntas.
    def perguntas(self):
        """
        """
        print("Algoritmo genético para o problema da mochila. /n Desenvolvido por Gabriel Cavalcante.")
        numItens = self.pergunta_1()
        self.pergunta_2(numItens)
        pergunta4Tamanho = self.pergunta_3()


# TESTES
main = Principal()
main.perguntas()
