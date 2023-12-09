import initialize, selection, crossover, mutation
import gym
n_genes = 6
moves = [0, 1, 2, 3]
gene_len = 10

def initialize_test(env):
    print(initialize.initialize_population(env, n_genes, gene_len))

def selection_test():
    population = initialize.initialize_population(n_genes, moves, gene_len)
    print(population)
    distances = [33, 60, 20, 3, 36, 34]
    heuristic = [round(100 / x, 2) for x in distances]
    print(heuristic)
    print(selection.rouletteWheelSelection(population, heuristic))

def crossover_test():
    population = initialize.initialize_population(n_genes, moves, gene_len)
    print(population)
    print(crossover.singlePointCrossover(population))

def mutation_test():
    population = initialize.initialize_population(n_genes, moves, gene_len)
    print(population)
    print(mutation.displacement_mutation(population))

env = gym.make(
    "MiniHack-Navigation-Custom-v0",
    observation_keys=("chars", "pixel"),
    des_file = "../complex_maze.des",
)
initialize_test(env)