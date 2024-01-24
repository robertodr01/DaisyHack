import copy
import copy
import random
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
 
def orderCrossover(population: [[]], shuffle_size=5):
    #shuffle_size = shuffle_size #round(len(population[0]) / 2)
    length =  len(population) - 1 if len(population) % 2 != 0 else len(population)
    for i in range(0, length, 2):
        firstGene = population[i]
        secondGene = population[i+1]
        # create list from 0 to size
        index = [*range(len(firstGene))] 
        # randomly select shuffle_size elements from index list
        bit_mask = set(random.sample(index, shuffle_size))
        inverse_bit_mask = set(index) - bit_mask

        newFirstGene = copy.deepcopy(firstGene)
        newSecondGene = copy.deepcopy(secondGene)


        for j in bit_mask:
            newFirstGene[j] = secondGene[j]
        for j in inverse_bit_mask:
            newSecondGene[j] = firstGene[j]

        for j, k in zip(inverse_bit_mask, bit_mask):
            newFirstGene[j] = firstGene[k]
        for j, k in zip(inverse_bit_mask, bit_mask):
            newSecondGene[k] = secondGene[j]


        population[i] = newFirstGene
        population[i+1] = newSecondGene
    return population
