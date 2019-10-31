import fitness

## geral num aleatŕop para ver se vai cruzar

# alpha = número aleatório entre 0 e 1, diferente pra cada casal
children = [[7.917, 7.917], [1, 1]]
fitnessVec = []
for child in children:
    value = fitness.calculateFitness([child[0], child[1]])
    fitnessVec.append(value)
    
print (fitnessVec)


# faz a roleta pra pegar quais os genes que vao cruzar;
      #
# para cada casal selecionado, usa a taxa de cruzamento pra ver se vai cruzar;

# se for cruzar:
      # cruzamento
            # x1filho1 = (alpha * x1pai1) + ((1 - alpha) * x1pai2)
            # x1filho2 = (alpha * x1pai2) + ((1 - alpha) * x1pai1)
            # x2 faz igual o x1
# se não
      # repete o casal


# depois do cruzamento, usa a taxa de mutação para ver se vai mutar PRA X1 E PRA X2 SEPARADO
# se for mutar:
      # muta
# se não for:
      # não muta