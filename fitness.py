import math


def calculateFitness(xVec):
    prod = 1
    for x in xVec:
        prod *= math.sqrt(x)*math.sin(x)
    prod += 7  # adding 10 so fitness will never be a negative value
    prod = round(prod, 3)
    print(prod)
    return prod

def calculatePopulationFitness(population, size):
    fitnessSum = 0
    for i in range(size):
        fitness = calculateFitness([population[i][0], population[i][1]])
        fitnessSum += fitness
        population[i][2] = fitness
        population[i][3] = fitnessSum
    return population

# print(calculateFitness([7.917, 7.917]))