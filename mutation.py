import random

def mutate(population, size, rate):
    for i in range(size):
        for j in range(2):
            rand = round(random.uniform(0, 1), 1)
            if(rand <= rate):
                population[i][j] = makeMutation(population[i][j])
    
    return population

def makeMutation(value):
    rand = round(random.uniform(-1, 1), 1)
    print("mutated value: " + str(rand))
    print("\told value: " + str(value))
    value = round((value + rand), 3)
    print("\tnew value: " + str(value))
    return value