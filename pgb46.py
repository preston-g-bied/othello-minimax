import math
import random
import time

import game

import othello
from othello import State

class pgb46(game.Player):
    def __init__(self, time_limit: int):
        super().__init__()
        self.time_limit = time_limit / 1000.0   # ms to s

    def choose_move(self, state: State):
        start_time = time.time()
        best_move = None
        depth = 1
        # PLAYER1 (O) = 0: wants to maximize
        # PLAYER2 (X) = 1: wants to minimize
        is_max_player = (state.nextPlayerToMove == othello.PLAYER1)
        
        # iterative deepening
        while True:
            elapsed = time.time() - start_time

            # check if enough for another iteration
            if elapsed >= self.time_limit * 0.90:
                break

            try:
                # try to search at current depth
                _, move = self.minimax(state, depth, is_max_player, float('-inf'), float('inf'), start_time)
                if move is not None:
                    best_move = move
                depth += 1
            except TimeoutError:
                # time ran out during search
                break

        return best_move
    
    def minimax(self, state: State, depth: int, max_player: bool, alpha: float, beta: float, start_time: float):
        # check time limit
        elapsed = time.time() - start_time
        if elapsed >= self.time_limit * 0.95:   # check if 5% of time remaining
            raise TimeoutError("Time limit reached")

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
                value, _ = self.minimax(state.applyMoveCloning(move), depth - 1, False, alpha, beta, start_time)
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
                value, _ = self.minimax(state.applyMoveCloning(move), depth - 1, True, alpha, beta, start_time)
                # see if new eval is better (smaller) thn current min
                if value < min_value:
                    min_value = value
                    best_move = move
                    beta = min(beta, min_value)
                if min_value <= alpha:
                    return min_value, best_move
            return min_value, best_move