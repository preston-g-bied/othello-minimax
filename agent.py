import math
import random

import game

class HumanPlayer(game.Player):

    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()

        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        response = input('Please choose a move: ')
        return moves[int(response)]

class RandomAgent(game.Player):
    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate possible moves
        moves = state.generateMoves()

        # if no available moves, pass
        if len(moves) == 0:
            return None

        # pick a random move from the moves list
        return random.choice(moves)


class MinimaxAgent(game.Player):
    pass


class AlphaBeta(game.Player):
    pass