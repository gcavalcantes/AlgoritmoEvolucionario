'''
Algoritmo Evolucionário - por Gabriel Cavalcante

Classe responsável por tratar o problema com um algoritmo evolutivo.
'''
from Cromossomo import Cromossomo
import random, time

class Evo():
    # Método __init__
    def __init__(self, tam_pop = 20, geracoes = 1000):
        
        self.pop = []
        self.tam_populacao = tam_pop
        self.geracoes = geracoes
        self.soma_avaliacoes = 0

    # Criar métodos de manipulação de população.
    def popular(self):
        for i in range(self.tam_populacao):
            self.pop.append(Cromossomo(10))
        for cromossomo in self.pop: 
            cromossomo.inicia()

    # Método para avaliação da população.
    def avalia(self):
        self.soma_avaliacoes = 0
        for Cromossomo in self.pop:
            self.soma_avaliacoes += Cromossomo.avalia()

    # Método de seleção entre os indivíduos avaliados.
    def escolha(self):
        self.avalia()
        max = random.random() * self.soma_avaliacoes
        i, aux = [0, 0]
        random.shuffle(self.pop)
        while aux < max and i < self.tam_populacao:
            aux += self.pop[i].avalia
            i += 1
        i -= 1
        return i
    
    # Método para selecionar pais.
    def nova_g(self):
        nova_pop = []
        for i in range(self.tam_populacao):
            pai1 = self.pop[self.escolha()]
            pai2 = self.pop[self.escolha()]
            filho = pai1.crossover(pai2)
            filho.mutacao(.05)
            nova_pop.append(filho)
        return nova_pop
    
    # TODO Método de inicialização da classe.
    def algo_genetico(self):
        print("====================\nSimulação de mutação genético\n====================")
        self.popular()
        self.avalia()
        ordem = sorted(self.pop, key = lambda x: x.avalia, reverse = True)
        for i in range(self.geracoes):
            top1 = ordem[0]
            top2 = ordem[1]
            top3 = ordem[2]
            top4 = ordem[3]
            top4 = ordem[4]
            top5 = ordem[4]
            print("Cinco melhroes da geração %d:\n%s\n%s\n%s\n%s\n%s\n\n" % (i, top1, top2, top3, top4, top5), end="", flush = True)
            time.sleep(.5)

            self.pop = self.nova_g()
            self.avalia()
            ordem = sorted(self.pop, key = lambda x: x.avalia, reverse = True)
        print('Melhor avaliado -> %s' % (ordem[1]))

# Nova instância para executar algoritmo
evolucao = Evo(tam_pop = 40, geracoes = 5)
evolucao.algo_genetico()