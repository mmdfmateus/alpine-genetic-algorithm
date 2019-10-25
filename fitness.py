import math


def calculateFitness(xVec):
    prod = 1
    for x in xVec:
        prod *= math.sqrt(x)*math.sin(x)
    return prod

calculateFitness([7.917, 7.917])