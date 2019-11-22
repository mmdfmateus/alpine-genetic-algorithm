import math


def calculateFitness(xVec):
    return 0.0001 * (abs(math.sin(xVec[0]) * math.sin(xVec[1]) * math.exp(abs(100-((math.sqrt(xVec[0]**2 + xVec[1]**2) ) / math.pi ) ) ) ) + 1 )**0.1


def calculatePopulationFitness(population, size):
    fitnessSum = 0
    populationAux = []
    for i in range(size):
        populationAux.append([])
        populationAux[i].append(population[i][0])
        populationAux[i].append(population[i][1])
    # print(population)
    for i in range(size):
        fitness = calculateFitness([population[i][0], population[i][1]])
        fitnessSum += fitness
        populationAux[i].append(fitness)
        populationAux[i].append(fitnessSum)
    return populationAux