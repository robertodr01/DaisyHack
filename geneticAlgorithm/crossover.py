def singlePointCrossover(population: [[]]):
    if(len(population)<1):
        raise ValueError()
    point = round(len(population[0]) / 2)

    for i in range(len(population), 2):
        firstGene = population[i]
        secondGene = population[i+1]
        newFirstGene = firstGene[:point] + secondGene[point:]
        newSecondGene = secondGene[:point] + firstGene[point:]
        population[i] = newFirstGene
        population[i+1] = newSecondGene

    