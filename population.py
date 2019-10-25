import random

def createPopulation(size):
    population = [[0 for x in range(4)] for y in range(size)]

    for i in range(size):
        population[i][0] = random.randint(0, 10)
        population[i][1] = random.randint(0, 10)
    return population

print(createPopulation(10))