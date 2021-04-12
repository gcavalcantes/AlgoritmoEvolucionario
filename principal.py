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
    # Variável para o valor do item na pergunta 2. Deve ser int.
    pergunta2Valor = 0
    # Variável para o peso do item na pergunta 2. Deve ser float.
    pergunta2Peso = 0.0

    # TODO Função para fazer as perguntas.
    def perguntas(self):
        """
        """
        print("Algoritmo genético para o problema da mochila. /n Desenvolvido por Gabriel Cavalcante.")
        numItens = pergunta_1()
        pergunta_2(numItens)
        pergunta_3()

    # TODO Função para a pergunta 1
    def pergunta_1(self):
        """
        Função que retorna o número de itens que será usado na solução e também pelos outros métodos da classe.
        """

        try:
            pergunta1 = int(input(
                print("Quantos itens terá a lista? (Número inteiro)")))
            while (pergunta1 < 2):
                print("Valor dever ser maior que um.")
                pergunta1 = int(input(
                    print("Quantos itens terá a lista? (Número inteiro) ")))
        except ValueError:
            print('Erro: Resposta precisa ser um número inteiro.')

        return pergunta1

    # TODO Função para a pergunta 2
    def pergunta_2(self, numItens):
        """
        """

        contador = 1
        try:
            # Loop para a segunda pergunta.
            while contador <= numItens:
                pergunta2Valor = int(input(
                    print('Qual o valor do item {}?').format(contador)))
                pergunta2Peso = float(
                    input(print('Qual o peso do item {}?').format(contador)))
                contador += 1
        # Tratamento de erro para caso a pergunta não seja um inteiro.
        except ValueError as ve:
            print('Erro: Resposta precisa ser um número inteiro.')

    # TODO Função para a pergunta 3
    def pergunta_3(self):
        """
        Função responsável por definir o tamanho da mochila
        """
