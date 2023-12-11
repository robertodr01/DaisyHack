import gym
import minihack
from geneticAlgorithm import initialize, selection, crossover, mutation
from tqdm import tqdm
import random
from utilsMinihackSearch import get_player_location, get_target_location, get_valid_moves, actions_from_path, manhattan_distance, is_wall, euclidean_distance
def get_wall(game_map, move):
    action_map = {
        "N": 0,
        "E": 1,
        "S": 2,
        "W": 3
    }
    x, y = get_player_location(game_map)
    element = ''
    if move == action_map["N"]:
        element = game_map[x, y-1]
    elif move == action_map["E"]:
        element = game_map[x+1, y]
    elif move == action_map["S"]:
        element = game_map[x, y+1]
    elif move == action_map["W"]:
        element = game_map[x-1, y]
    return is_wall(element)

def get_available_actions(game_map):
    player_location = get_player_location(game_map)
    available_moves = get_valid_moves(game_map, player_location)
    available_actions = [actions_from_path(player_location, [move])[0] for move in available_moves]
    return available_actions

def heuristic1(env, path):
    points = 0
    state = env.reset()
    game_map = state['chars']
    init_player_location = get_player_location(game_map)
    for move in path:
        state, _, done, _ = env.step(move)
        if done:
            return 10001
        game_map = state['chars']
    player_location = get_player_location(game_map)
    points +=  round(manhattan_distance(player_location, init_player_location), 2)
    return points
def heuristic2(env, path):
    extra_points = 0
    points = 0
    state = env.reset()
    game_map = state['chars']
    target_location = get_target_location(game_map)
    for move in path:
        state, _, done, _ = env.step(move)
        if done:
            return 10001
        player_location = get_player_location(game_map)
        if manhattan_distance(player_location, target_location) < 5:
            extra_points = 1000
        game_map = state['chars']
    player_location = get_player_location(game_map)
    points += 5 * round(20/manhattan_distance(player_location, target_location), 2)
    return points + extra_points

def core(epochs, paths, substring_length, env, length_new_population = None, shuffle_size = 5, heuristic: callable = heuristic1, entropy = 0.5, prefix=[]):
    best_path = []
    best_points = 0
    heuristic_results = [1]*len(paths)
    for i in tqdm(range(epochs)):
        f = open("logs.txt", "a")
        paths = selection.rouletteWheelSelection(paths, heuristic_results, length_new_population)
        paths = crossover.singlePointCrossover(paths)
        if entropy > 0.5:
            paths = crossover.order_crossover(paths, shuffle_size)
        else:
            paths = crossover.singlePointCrossover(paths)
        paths = mutation.displacement_mutation(paths, substring_length)
        f.write(f"{i+1} generation: ")
        heuristic_results = []
        for path in paths:
            points = heuristic(env, prefix + path)
            if points > best_points:
                best_points = points
                best_path = path
            f.write(f"{points} ")
            heuristic_results.append(points)
        f.write(f"\n")
        f.close()
    return paths, best_path

def ga(env_opts, n_genes, path_length, epochs, substring_length, shuffle_size = 5, queue=None):
    env = gym.make(
        env_opts["id"],
        observation_keys=env_opts["observation_keys"],
        des_file = env_opts["des_file"],
    )
    epochs_unit = round(epochs/3)
    path_unit = round(path_length/2)
    paths = initialize.initialize_population(env, n_genes, path_unit, get_available_actions)
    paths, prefix = core(epochs_unit, paths, substring_length, env, shuffle_size = shuffle_size,heuristic=heuristic1, entropy=0.6)
    paths = initialize.initialize_population(env, n_genes, path_unit, get_available_actions)
    paths, best_path = core(2 * epochs_unit, paths, substring_length, env, shuffle_size = shuffle_size, heuristic=heuristic2, entropy=0.6, prefix=prefix)
    if queue:
        for path in paths:
            queue.put(prefix + path)
        queue.put(prefix + best_path)
    else:
        return [prefix + path for path in paths], prefix + best_path