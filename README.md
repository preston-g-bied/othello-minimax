I implented the following Othello agents:
1. **Random Agent:** This agent selects a random legal move from all available moves.
2. **Minimax Agent:** This agent uses the Minimax algorithm to search the game tree up to a specified depth, alternating between maximizing (Player O) and minimizing (Player X) the board score function.
3. **AlphaBeta Agent:** This agent implements Minimax with alpha-beta pruning.
4. **Extra Agent:** This agent uses a time limit with by alpha-beta algorithm and a depth-limited search style.

The minimax algorithm has a time complexity of O(b^d), where b is the branching factor and d is the search depth. Alpha-beta pruning reduces the effective complexity to O(b^(d/2)) in the best case by eliminating branches that cannot affect the outcome.