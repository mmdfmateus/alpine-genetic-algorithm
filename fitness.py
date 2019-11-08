import math


def calculateFitness(xVec):
    prod = 1
    for x in xVec:
        prod *= math.sqrt(x)*math.sin(x)
    prod += 7  # adding 7 so fitness will never be a negative value
    prod = round(prod, 4)
    return prod

def calculatePopulationFitness(population, size):
    fitnessSum = 0
    for i in range(size):
        fitness = calculateFitness([population[i][0], population[i][1]])
        fitnessSum += fitness
        population[i][2] = fitness
        population[i][3] = round (fitnessSum, 4)
    return population

# print(calculateFitness([8, 5]))