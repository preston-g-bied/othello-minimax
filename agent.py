import math
import random

import game

from othello import State

class HumanPlayer(game.Player):

    def __init__(self):
        super().__init__()

    def choose_move(self, state: State):
        # generate the list of moves:
        moves = state.generateMoves()

        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        response = input('Please choose a move: ')
        return moves[int(response)]

class RandomAgent(game.Player):
    def __init__(self):
        super().__init__()

    def choose_move(self, state: State):
        # generate possible moves
        moves = state.generateMoves()

        # if no available moves, pass
        if len(moves) == 0:
            return None

        # pick a random move from the moves list
        return random.choice(moves)


class MinimaxAgent(game.Player):
    def __init__(self, depth: int = 3):
        super().__init__()
        self.depth = depth

    def choose_move(self, state: State):
        # PLAYER1 (O) = 0: wants to maximize
        # PLAYER2 (X) = 1: wants to minimize
        is_max_player = (state.nextPlayerToMove == 0)
        _, best_move = self.minimax(state, self.depth, is_max_player)
        return best_move
    
    def minimax(self, state: State, depth: int, max_player: bool):
        # if terminal state or max depth reached, return utility function (score)
        if state.game_over() or depth == 0:
            return state.score(), None
        
        # generate moves
        moves = state.generateMoves()
        if len(moves) == 0:
            moves = [None]
        
        if max_player:
            max_value = float('-inf')
            best_move = None
            # loop through possible moves
            for move in moves:
                # apply move and pass to min_player, with decreased depth
                value, _ = self.minimax(state.applyMoveCloning(move), depth - 1, False)
                # see if new eval is better (bigger) than current max
                if value > max_value:
                    max_value = value
                    best_move = move
            return max_value, best_move
        else:
            # else you are min_player
            min_value = float('inf')
            best_move = None
            # loop through possible moves
            for move in moves:
                # apply move and pass to max_player, with decreased depth
                value, _ = self.minimax(state.applyMoveCloning(move), depth - 1, True)
                # see if new eval is better (smaller) thn current min
                if value < min_value:
                    min_value = value
                    best_move = move
            return min_value, best_move

class AlphaBeta(game.Player):
    def __init__(self, depth: int = 3):
        super().__init__()
        self.depth = depth

    def choose_move(self, state: State):
        # PLAYER1 (O) = 0: wants to maximize
        # PLAYER2 (X) = 1: wants to minimize
        is_max_player = (state.nextPlayerToMove == 0)
        _, best_move = self.minimax(state, self.depth, is_max_player, float('-inf'), float('inf'))
        return best_move
    
    def minimax(self, state: State, depth: int, max_player: bool, alpha: float, beta: float):
        # if terminal state or max depth reached, return utility function (score)
        if state.game_over() or depth == 0:
            return state.score(), None
        
        # generate moves
        moves = state.generateMoves()
        if len(moves) == 0:
            moves = [None]
        
        if max_player:
            max_value = float('-inf')
            best_move = None
            # loop through possible moves
            for move in moves:
                # apply move and pass to min_player, with decreased depth
                value, _ = self.minimax(state.applyMoveCloning(move), depth - 1, False, alpha, beta)
                # see if new eval is better (bigger) than current max
                if value > max_value:
                    max_value = value
                    best_move = move
                    alpha = max(alpha, max_value)
                if max_value >= beta:
                    return max_value, best_move
            return max_value, best_move
        else:
            # else you are min_player
            min_value = float('inf')
            best_move = None
            # loop through possible moves
            for move in moves:
                # apply move and pass to max_player, with decreased depth
                value, _ = self.minimax(state.applyMoveCloning(move), depth - 1, True, alpha, beta)
                # see if new eval is better (smaller) thn current min
                if value < min_value:
                    min_value = value
                    best_move = move
                    beta = min(beta, min_value)
                if min_value <= alpha:
                    return min_value, best_move
            return min_value, best_move