from population import Population
import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


population = Population()

def train():
    population.evaluate()
    population.selection()
    print(population.getTotalSequence())

# train()
set_interval(train, 1)










# target = 'abcdefghij'

# popul = Population()
# populist = popul.getTotalSequence()
# population = popul.getTotal()

# # print(populist)


# mating_pool = []
# # evaluate fitness
# for i in range(len(populist)):
#     maxfitness = 0
#     count = 0

#     for j in range(len(populist[i])):
#         if target[j] == populist[i][j]:
#             count += 1
#         else:
#             if count > maxfitness:
#                 maxfitness = count
#             count = 0
        
#     fitness = maxfitness / 10

#     population[i].setFitness(fitness)

#     n = int(population[i].getFitness() * 100)
#     for k in range(n):
#         mating_pool.append(population[i])
        
# popul.setMatingPool(mating_pool)



    


# print(popul.getFitnessMapping())
# print(popul.getMatingPool())



