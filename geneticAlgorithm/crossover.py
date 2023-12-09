def singlePointCrossover(population: [[]]):
    if(len(population)<1):
        raise ValueError()
    point = round(len(population[0]) / 2)
    length =  len(population) - 1 if len(population) % 2 != 0 else len(population) 
    for i in range(0, length, 2):
        firstGene = population[i]
        secondGene = population[i+1]
        newFirstGene = firstGene[:point] + secondGene[point:]
        newSecondGene = secondGene[:point] + firstGene[point:]
        population[i] = newFirstGene
        population[i+1] = newSecondGene
    return population

    