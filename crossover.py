import fitness

## geral num aleatŕop para ver se vai cruzar

# alpha = número aleatório
children = [[7.917, 7.917], [1, 1]]
fitnessVec = []
for child in children:
    value = fitness.calculateFitness([child[0], child[1]])
    fitnessVec.append(value)
    
print (fitnessVec)

#cruzamento
# x1f1 = (alpha * x1p1) + ((1 - alpha) * x1p2)
# x1f2 = (alpha * x1p2) + ((1 - alpha) * x1p1)