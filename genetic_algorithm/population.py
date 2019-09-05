from string import String
from random import choice

class Population:
    def __init__(self):
        self.popsize = 100
        self.total = [String() for i in range(self.popsize)]
        self.mating_pool = []
        # self.target = 'wertygvhbjskdnasdnhjbqjwe'
        # self.target = 'abcdefghij'
        self.target = 'abcdefghijklmnopqrstuvwxyz'
        # self.target = 'dfghasujdkqwjwqejqkwensakm'
    
    def getTotalSequence(self):
        return [self.total[i].getSequence() for i in range(len(self.total))]
    
    def getFitnessMapping(self):
        return {self.total[i].getSequence():self.total[i].getFitness() for i in range(len(self.total))}
    
    def getTotal(self):
        return self.total

    def selection(self):
        new_population = []
        for i in range(len(self.total)):
            parentA = choice(self.mating_pool)
            parentB = choice(self.mating_pool)
            child = parentA.crossover(parentB)
            child.mutation()
            new_population.append(child)


        self.total = new_population


    def evaluate(self):
        populist = self.getTotalSequence()
        mating_pool = []
        # print(populist)

        # evaluate fitness
        for i in range(len(populist)):
            # maxfitness = 0
            count = 1

            for j in range(len(populist[i])):
                if self.target[j] != populist[i][j]:
                    count *= 2
                # else:
                #     if count > maxfitness:
                #         maxfitness = count
                #     count = 1
                
            fitness = 1.0 / count
            # print('fitness = ' + str(fitness))
            # unnormalized fitness
            self.total[i].fitness = fitness

        # find maximum fitness
        maxfit = 0
        for i in range(len(self.total)):
            if self.total[i].fitness > maxfit:
                maxfit = self.total[i].fitness
        
        print('==========================================' + str(maxfit) + '==========================================')
        # normalize fitness between 0-1
        for i in range(len(self.total)):
            self.total[i].fitness /= maxfit
            # print('normalized = ' + str(self.total[i].fitness))




        for i in range(len(self.total)):
            n = round(self.total[i].fitness * 100)
            # print('self fitness = ' + str(self.total[i].fitness))
            # print(n)
            # print('self fitness = ' + str(self.total[i].fitness))
            for k in range(n):
                mating_pool.append(self.total[i])
        
        # print(mating_pool)
        self.mating_pool = mating_pool
        

    


