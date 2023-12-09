import random
import gym
def inizialize_gene(env: gym.Env, gene_length: int, get_available_actions: callable) -> [int]:
    gene = []
    state = env.reset()
    for _ in range(gene_length):
        game_map = state['chars']
        moves = get_available_actions(game_map)
        move = random.randint(0, len(moves) - 1)
        env.step(moves[move])
        gene.append(moves[move])
    return gene

def initialize_population(env: gym.Env,n_genes: int, gene_length: int, get_available_actions: callable) -> [[int]]:
    population = []
    for _ in range(n_genes):
        gene = inizialize_gene(env, gene_length, get_available_actions)
        population.append(gene)
    return population