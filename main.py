import population, fitness, selection, crossover, mutation, maxmin

mutationRate = 0.1
crossoverRate = 0.7

size = 10

print("\n### INITIAL POPULATION ###\n")
currentPopulation = population.createPopulation(size)
print(currentPopulation)
print()

for i in range(100):
    input()
    print("\n### POPULATION FITNESS ###")
    currentPopulation = fitness.calculatePopulationFitness(currentPopulation, size)
    print()
    print(currentPopulation)


    print()
    print("\n### CALCULATE MAX MIN ###")
    max = maxmin.calculateMax(currentPopulation)
    min = maxmin.calculateMin(currentPopulation)
    med = maxmin.calculateMed(currentPopulation, size)
    print('Max value: ' + str(max))
    print('Med value: ' + str(med))
    print('Min value: ' + str(min))

    print()
    fathers = selection.rouletteSelection(currentPopulation, size)

    print()

    currentPopulation = crossover.crossover(fathers, size, crossoverRate)
    print("\n### POPULATION AFTER CROSSOVER ###")
    print(currentPopulation)

    print()
    currentPopulation = mutation.mutate(currentPopulation, size, mutationRate)
    print("\n### POPULATION AFTER MUTATION ###")
    print(currentPopulation)

    print()
    print('### MAX and MIN values ###')
    print('Max value: ' + str(max))
    print('Med value: ' + str(med))
    print('Min value: ' + str(min))