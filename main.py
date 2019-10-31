import population, fitness, selection

mutationRate = 0.1
crossoverRate = 0.7

size = 10

print("\n### INITIAL POPULATION ###\n")
currentPopulation = population.createPopulation(size)
print(currentPopulation)
print()
print("\n### POPULATION FITNESS ###")
currentPopulation = fitness.calculatePopulationFitness(currentPopulation, size)
print()
print(currentPopulation)

print()
selection.rouletteSelection(currentPopulation, size)