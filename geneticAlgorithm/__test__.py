import initialize, selection, crossover, mutation
import gym
import minihack
n_genes = 2
moves = [0, 1, 2, 3]
gene_len = 6

def initialize_test(env):
    print(initialize.initialize_population(env, n_genes, gene_len))

def selection_test():
    population = initialize.initialize_population(n_genes, moves, gene_len)
    print(population)
    distances = [33, 60, 20, 3, 36, 34]
    heuristic = [round(100 / x, 2) for x in distances]
    print(heuristic)
    print(selection.rouletteWheelSelection(population, heuristic))

def crossover_test(env):
    population = initialize.initialize_population(env, n_genes, gene_len, lambda x: moves)
    print(population)
    print(crossover.singlePointCrossover(population))

def order_crossover_test(env):
    population = initialize.initialize_population(env, n_genes, gene_len, lambda x: moves)
    print(population[0])
    print(population[1])
    population = crossover.order_crossover(population, 3)
    print()
    print(population[0])
    print(population[1])

def mutation_test(env):
    population = initialize.initialize_population(env, n_genes, gene_len, lambda x: moves)
    print(mutation.displacement_mutation(population, gene_len/2 - 1))

env = gym.make(
    "MiniHack-Navigation-Custom-v0",
    observation_keys=("chars", "pixel"),
    des_file = "../complex_maze.des",
)
#crossover_test(env)
order_crossover_test(env)