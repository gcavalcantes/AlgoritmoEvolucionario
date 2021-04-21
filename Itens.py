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
        self.beneficio = 0
        self.fitness = fitness
        self.solucao1 = []
        self.solucao2 = []
        self.solucao3 = []
        self.solucao4 = []

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
            # Variável que recebe 0 ou 1
            num = random.randint(0, 1)
            # Lista da solução recebe 0 ou 1
            self.listaItem[contador] = num
            contador = contador + 1
        print('Lista final: {}'.format(self.listaItem))
        return self.listaItem

    listaDeItens = gerarItensNaLista(4)

    # Método para avaliação da lista. Esta avaliação tem como fitness o cálculo envolvendo o custo de produção, o tempo de produção e o lucro de cada item na lista.
    def avaliaResultado(self, lista):
        '''
        Método reponsável por fazer o cálculo de fitness de solução uma solução. Este método retorna um fitness final
        '''
        # Calculo do fitness de um item
        # O cálculo do benefício de um item na lista é feito diminuindo o custo do item pelo lucro e somando pelo tempo de produção. Quanto maior o número, maior o fitness
        contador = 0
        fimCalculo = False
        while fimCalculo == False & contador < 4:
            if lista[contador] != 0:
                # Variável benefício recebe
                self.beneficio += float(
                    (self.listaCusto[contador] - self.listLucro[contador]) + self.listaTempo[contador])
            else:
                self.beneficio += 0
            contador += 1
            print('A lista de benefícios ficou assim: \n{}'.format(self.beneficio))
            return self.beneficio

    # TODO Método para gerar várias listas que representam os soluções da geração atual
    def gerarListas():
        '''
        Método que utiliza as variáveis declaradas no início para armazenar as soluções da geração atual.
        '''
        return null
