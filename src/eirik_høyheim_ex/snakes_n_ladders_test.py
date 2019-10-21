from random import randint


def throw_dice():
    return randint(1, 6)


def single_game(num_players):
    snake_ladder = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                    24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    player_pos = [0] * num_players
    player_moves = [0] * num_players
    for game in range(num_players):

        while player_pos[game] < 90:
            player_pos[game] += throw_dice()

            if player_pos[game] in snake_ladder:
                player_pos[game] = snake_ladder[player_pos[game]]

            player_moves[game] += 1


def multiple_games(num_games, num_players):
    winner_numbers = []
    for games in range(num_games):
        winner_numbers.append(single_game(num_players))

    return winner_numbers
