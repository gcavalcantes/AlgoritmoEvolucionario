'''
Arquivo responsável por reunir todos os outros para o algoritmo genético.
'''

import ProblemaMochila
import Itens


class Principal():
    '''
    Classe principal do programa.
    '''
    # Variável para o número de itens na solução
    pergunta1 = 0
    # Variável para o valor de cada item na solução
    valorItem = 0

    # TODO Função para fazer as perguntas.
    def perguntas():
        """
        """
        print("Algoritmo genético para o problema da mochila. /n Desenvolvido por Gabriel Cavalcante.")
        pergunta_1()
        pergunta_2()
        pergunta3 = input(print(""))

    # TODO Função para a pergunta 1
    def pergunta_1():
        """
        Função que retorna o número de itens que será usado na solução e também pelos outros métodos da classe.
        """

        pergunta1
        try:
            pergunta1 = input(
                print("Quantos itens terá a lista? (Número inteiro)"))
            while (pergunta1 < 2):
                print("Valor dever ser maior que um.")
                pergunta1 = int(input(
                    print("Quantos itens terá a lista? (Número inteiro)")))
        except ValueError:
            print('Erro: Resposta precisa ser um número inteiro.')

        return pergunta1

    # TODO Função para a pergunta 2
    def pergunta_2(self, numItens):
        """
        """
        pergunta2
        contador = 1
        while contador <= numItens:
            print('Qual o valor do intem {}'.format(numItens))
            pergunta2 = input(print('Qual o valor do item?'))
