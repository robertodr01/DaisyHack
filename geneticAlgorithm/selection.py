import numpy as np
def rouletteWheelSelection(population: [[]], heuristic_results: [float], ):
    new_population = []
    total = sum(heuristic_results)
    propabilities = [value/total for value in heuristic_results]
    for _ in range(len(population)):
        new_population.append(np.random.choice(population, p=propabilities))