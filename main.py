import population, fitness, selection, crossover, mutation

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
fathers = selection.rouletteSelection(currentPopulation, size)

print()

currentPopulation = crossover.crossover(fathers, size, crossoverRate)
print("\n### POPULATION AFTER CROSSOVER ###")
print(currentPopulation)

print()
currentPopulation = mutation.mutate(currentPopulation, size, mutationRate)
print("\n### POPULATION AFTER MUTATION ###")
print(currentPopulation)

