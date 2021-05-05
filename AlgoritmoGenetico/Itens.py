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

    def __init__(self):
        '''
        Construto de OOP que cria um objeto quando a classe é chamada
                e é passado como o primeiro parâmetro deste método.
        '''
        self.nomesDosItens = ['Sandálias', 'Sapatos',
                              'Botas femininas', 'Sapatos femininos']
        self.listaCusto = [100.0, 120.0, 150.0, 120.0]
        self.listaTempo = [20.0, 30.0, 25.0, 28.0]
        self.listLucro = [60.0, 80.0, 90.0, 50.0]
        # Variável para a lista de materias primas usadas.
        self.listaItem = []
        # Variável fitness de uma solução
        self.beneficio = 0
        # Variável para as listas na geração atual
        self.solucao = []
        # Variável para o fitness de cada solução
        self.fitness = 0
        # Variáveis para os pais da geração atual
        self.pai1 = []
        self.pai2 = []
        # Variáveis para os filhos
        self.filho1 = []
        self.filho2 = []

    # Gera uma lista de soluções

    def gerarItensNaLista(self, quantidadeDeItens):
        '''
        Decide quais os itens que estão disponíveis em uma solução
        '''
        maxMateriaPrima = 400
        contador = 0
        while contador <= quantidadeDeItens:
            # Variável que recebe um número entre 0 e 400
            num = random.randint(0, maxMateriaPrima)
            # Lista da solução recebe 0 até a materia prima disponível
            self.listaItem[contador] = num
            contador = contador + 1
            maxMateriaPrima -= num
        print('Lista final: {}'.format(listaItem))
        return self.listaItem

    # Método para avaliação da lista. Esta avaliação tem como fitness o cálculo envolvendo o custo de produção, o tempo de produção e o lucro de cada item na lista.
    def avaliaResultado(self, lista):
        '''
        Método reponsável por fazer o cálculo de fitness de solução uma solução. Este método retorna um fitness final
        '''
        # Calculo do fitness de um item
        # O cálculo do benefício de um item na lista é feito diminuindo o custo do item pelo lucro e somando pelo tempo de produção. Quanto maior o número, maior o fitness
        contador = 0
        while contador < 4:
            if lista[contador] != 0:
                # Variável benefício recebe
                beneficio += float(
                    (self.listaCusto[contador] - self.listLucro[contador]) + self.listaTempo[contador])
            else:
                self.beneficio += 0
            contador += 1
            print('A lista de benefícios ficou assim: \n{}'.format(self.beneficio))
            return self.beneficio

    # Método para gerar várias listas que representam os soluções da geração atual
    def gerarListasIniciais(self):
        '''
        Método que utiliza as variáveis declaradas no início para armazenar as soluções da geração atual.
        Os resultados são então avaliados usando o método de avaliação.
        '''
        # Geração das soluções
        contador = 0
        while contador < 4:
            self.solucao[contador] = Itens.gerarItensNaLista(4)
            print('Solução gerada: {}\n'.format(self.solucao))

        # Avaliação das soluções
        contador = 0
        while contador < 4:
            self.fitness[contador] = Itens.avaliaResultado(
                self.solucao[contador])

    # Método para selecionar os pais que gerarão a próxima geração.

    def selecionaPais(self):
        '''
        Método que utiliza aleatoriedade para decidir quais soluções serão
        '''
        # Variável de contagem e manipulação da lista
        contador = 0
        # Variáveis para armazenar um item que é pai.
        self.pai1 = []
        self.pai2 = []
        # Encontra o maior fitness na solução
        while contador < 4:
            # Se o fitness atual for maior que o próximo
            if self.fitness[contador] >= self.fitness[contador + 1]:
                pai1 = self.solucao[contador]
            contador += 1
        contador = 0
        # Encontra o menor fitness na solução
        while contador < 4:
            # Se o fitness atual for menor que o próximo
            if fitness[contador] >= fitness[contador + 1]:
                pai2 = self.solucao[contador]
            contador += 1

    # Método de crossover
    def crossover(self):
        # Filho 1 recebe genes aleatórios
        self.filho1 = []
        self.filho1.append(self.pai1[random.randint(0, 3)])
        self.filho1.append(self.pai1[random.randint(0, 3)])
        self.filho1.append(self.pai2[random.randint(0, 3)])
        self.filho1.append(self.pai2[random.randint(0, 3)])
        # Filho 2 recebe genes aleatórios
        self.filho2 = []
        self.filho2.append(self.pai2[random.randint(0, 3)])
        self.filho2.append(self.pai2[random.randint(0, 3)])
        self.filho2.append(self.pai1[random.randint(0, 3)])
        self.filho2.append(self.pai1[random.randint(0, 3)])

    # TODO Mutação
    def mutacao(self):
        return None

    # TODO Método para a nova geração
    def novaGeração(self):
        return None
