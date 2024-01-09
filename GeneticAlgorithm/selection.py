import numpy as np

def rouletteWheelSelection(population: [[]], heuristic_results: [float], length_new_population: int = None):
    new_population = []
    total = sum(heuristic_results)
    propabilities = [value/total for value in heuristic_results]
    length = length_new_population if length_new_population != None else len(population)
    for _ in range(length):
        index = np.random.choice(len(population), p=propabilities)
        new_population.append(population[index])
    return new_population