import random
def displacement_mutation(population: [[]]):
    if len(population) < 1:
        raise ValueError()
    substring_length = 3
    length = len(population[0]) - substring_length
    first_index = random.randint(0, length)
    second_index = random.randint(0, length)
    for i in range(len(population)):
        gene = population[i]
        substring = gene[first_index : first_index + substring_length]
        gene[first_index : first_index + substring_length] = gene[second_index : second_index + substring_length]
        gene[second_index : second_index + substring_length] = substring
