from Chromosome import Chromosome
from random import shuffle
class ComputeGA:
    def __init__(self,problParam,network):
        self.__problParam=problParam
        self.__net=network
        self.__population=self.initPopulation()

    def initPopulation(self):
        all=[]
        for el in range(self.__problParam['noChromos']):
            ch=Chromosome(self.__problParam)
            ch.calculate_fitness()
            all.append(ch)
        return all

    @property
    def population(self):
        return self.__population

    def new_gen(self):
        shuffle(self.population)
        my_new_pop=[]
        for el in range(0,len(self.__population)-1,2):
            c1=self.population[el]
            c2=self.population[el+1]
            newOff=c1.crossover(c2)
            newOff.mutation()
            newOff.calculate_fitness()
            my_new_pop.append(c1)
            my_new_pop.append(c2)
            my_new_pop.append(newOff)

        my_new_pop=sorted(my_new_pop, key= lambda chromo: chromo.fitness)
        n=self.__problParam['noChromos']/2
        i=0
        while i<n:
            my_new_pop.pop(-1)
            i+=1
        self.__population=my_new_pop
        print('best',self.__population[0])

    def get_best_chromo(self):
        self.__population=sorted(self.__population, key= lambda chromo: chromo.fitness)
        return self.__population[0]

    def compute_all(self):
        for el in range(self.__problParam['noGen']):
            print(el)
            self.new_gen()

    def write_to_file(self,file):
        f=open(file,"w+")
        best_cr=self.get_best_chromo()
        f.write("%d " % best_cr.fitness)
        f.write("\n")
        for el in best_cr.repres:
            f.write("%d " % el)
        f.close()


