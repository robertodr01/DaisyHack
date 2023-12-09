from utilsMinihackSearch import *
def test_actions_from_path(start, valid_moves):
    available_moves = [actions_from_path(start,[valid_move]) for valid_move in valid_moves]
    print(available_moves)
valid_moves = [(14, 22), (15, 23), (14, 24), (13, 23)]
player_location = (14, 23)
test_actions_from_path(player_location, valid_moves)