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
    # Variável que recebe o número de itens a serem criados
    # numItens = Principal.pergunta1

    # Método init
    def __init__(self):
        '''
        Construto de OOP que cria um objeto quando a classe é chamada
                e é passado como o primeiro parâmetro deste método.
        '''
        self.listaCusto = [100.0, 120.0, 150.0, 120.0]
        self.listaTempo = [20, 30, 25, 28]
        self.listLucro = [60.0, 80.0, 90.0, 50.0]
        self.listaItem = []
        self.beneficio = []
        self.fitness = fitness

    def gerarItens(self):
        '''
        Função responsável por criar lista de itens.
        '''
        itensExistentes = gerarItensNaLista()

    def gerarItensNaLista(self, quantidadeDeItens):
        '''
        Decide quais os itens que estão disponíveis em uma solução
        '''
        contador = 0
        while contador <= quantidadeDeItens:
            num = random.randint(0, 1)
            self.listaItem[contador] = num
            contador = contador + 1
        print('Lista final: {}'.format(self.listaItem))
        return self.listaItem

    listaDeItens = gerarItensNaLista(4)

    # TODO Método para avaliação da lista. Esta avaliação tem como fitness o cálculo envolvendo o custo de produção, o tempo de produção e o lucro de cada item na lista.
    def avaliaResultado(self, lista):
        '''
        Método reponsável por fazer o cálculo de fitness de solução uma solução. Este método retorna um fitness final
        '''
        # TODO Calculo do fitness de um item
        # O cálculo do benefício de um item na lista é feito diminuindo o custo do item pelo lucro e somando pelo tempo de produção. Quanto maior o número, maior o fitness
        contador = 0
        fimCalculo = False
        while fimCalculo == False & contador < 4:
            # Variável benefício recebe
            self.beneficio[contador] = float(
                (self.listaCusto[contador] - self.listLucro[contador]) + self.listaTempo[contador])
            contador += 1
