from utilsMinihackSearch import *
from ga import *
import os
import gym
import minihack

def test_actions_from_path(start, valid_moves):
    available_moves = [actions_from_path(start,[valid_move]) for valid_move in valid_moves]
    print(available_moves)

def test_ga():
    env_opts = {
        "id": "MiniHack-Navigation-Custom-v0",
        "des_file": "complex_maze.des",
        "observation_keys": ("chars", "pixel"),
    }
    #genetic parameters
    epochs = 5
    n_genes = 15
    path_length = 70
    #mutation parameters
    substring_length = 23
    #crossover parameters
    shuffle_size = 35
    paths = ga(env_opts, n_genes, path_length, epochs, substring_length, shuffle_size = shuffle_size)
    print(paths)
    
def test_initialize():
    env_opts = {
        "id": "MiniHack-Navigation-Custom-v0",
        "des_file": "complex_maze.des",
        "observation_keys": ("chars", "pixel"),
    }
    env = gym.make(
        env_opts["id"],
        observation_keys=env_opts["observation_keys"],
        des_file = env_opts["des_file"],
    )
    population = initialize.initialize_population(env, 4, 25, get_available_actions)
    print()
    for gene in population:
        print()
        print(gene)
    print()
    print()

def test_order_crossover():
    env_opts = {
        "id": "MiniHack-Navigation-Custom-v0",
        "des_file": "complex_maze.des",
        "observation_keys": ("chars", "pixel"),
    }
    env = gym.make(
        env_opts["id"],
        observation_keys=env_opts["observation_keys"],
        des_file = env_opts["des_file"],
    )
    population = initialize.initialize_population(env, 2, 24, get_available_actions)
    population = crossover.order_crossover(population, shuffle_size=12)

def test_single_point_crossover():
    env_opts = {
        "id": "MiniHack-Navigation-Custom-v0",
        "des_file": "complex_maze.des",
        "observation_keys": ("chars", "pixel"),
    }
    env = gym.make(
        env_opts["id"],
        observation_keys=env_opts["observation_keys"],
        des_file = env_opts["des_file"],
    )
    population = initialize.initialize_population(env, 2, 24, get_available_actions)
    population = mutation.displacement_mutation(population, )
test_order_crossover()

# valid_moves = [(14, 22), (15, 23), (14, 24), (13, 23)]
# player_location = (14, 23)
# test_actions_from_path(player_location, valid_moves)