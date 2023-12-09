import numpy as np

def rouletteWheelSelection(population: [[]], heuristic_results: [float], ):
    new_population = []
    total = sum(heuristic_results)
    propabilities = [value/total for value in heuristic_results]
    length = len(population)
    for _ in range(length):
        index = np.random.choice(length, p=propabilities)
        new_population.append(population[index])
    return new_population