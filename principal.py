'''
Arquivo responsável por reunir todos os outros para o algoritmo genético.
'''


class Principal():
    '''
    Classe principal do programa.
    '''


    # Variável para o número de itens na solução
int pergunta1
# Variável para o valor de cada item na solução
int pergunta2

# TODO Função para fazer as perguntas.


def perguntas():
		"""
		"""
		print("Algoritmo genético para o problema da mochila. /nDesenvolvido por Gabriel Cavalcante.")
		pergunta_1()
		pergunta_2()
		String pergunta3 = input(print("")

                           # Função para a pergunta 1
                           def pergunta_1():
                           """
		Função que retorna o número de itens que será usado na solução e também pelos outros médotos da classe.
		"""
        int pergunta1
        try:
        pergunta1=val(input(print("Quantos itens terá a lista? (Número inteiro)"))
                        while (pergunta1 < 2):
                        print("Valor deve ser maior que um")
                        pergunta1=val(input(print("Quantos itens terá a lista? (Número inteiro)"))
                                                       except ValueError:
                                                       print(
                                             'ERRO: Resposta precisa ser um número inteiro.')

                               return pergunta1

                               # TODO Função para a pergunta 2
                               def pergunta_2(int numItens):
                               """
		"""
                               int pergunta2
                               int contador=1
                               while contador <= numItens:
                               print("Qual o valor do item {}".format(numItens))
                               pergunta2=input(
                                             print("Qual o valor do item?"))
