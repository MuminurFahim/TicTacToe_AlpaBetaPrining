import variables
import core_func
from random import choice


def human_turn():
    return core_func.correct_input(variables.get_coordinate_message + variables.symbol, core_func.availables())


def random_turn():
    return choice(core_func.availables())


# alpha - maximizer's max - it should be less than its parent node minimizer's min
# beta - minimizer's min - it should be greater than its parent node maximizer's max


def minimax(depth, alpha, beta):
    new_depth = depth + 1
    avails = core_func.availables()
    if new_depth % 2:  # maximizer
        if core_func.check_win():
            return -1, depth  # previously minimizer
        elif not avails:
            return 0, depth
        best_score = -float('inf'), -float('inf')
        for c in avails:
            i = c - 1
            variables.grid[i] = variables.symbol
            t = tuple(variables.grid)
            if t in variables.states:
                score = variables.states[t]
            else:
                score = minimax(new_depth, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            variables.grid[i] = c
            if beta <= alpha: break
    else:  # minimizer
        if core_func.check_win():
            return 1, -depth  # previously maximizer
        elif not avails:
            return 0, -depth
        opponent = variables.valid_symbols - {variables.symbol}
        opponent = opponent.pop()
        best_score = float('inf'), float('inf')
        for c in avails:
            i = c - 1
            variables.grid[i] = opponent
            t = tuple(variables.grid)
            if t in variables.states:
                score = variables.states[t]
            else:
                score = minimax(new_depth, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            variables.grid[i] = c
            if beta <= alpha: break
    if c == avails[-1]:
        t = tuple(variables.grid)
        variables.states[t] = best_score
    return best_score


def perfect_turn():
    max_score = -float('inf'), -float('inf')
    coordinate = None
    for c in variables.grid:
        if c in variables.valid_symbols: continue
        i = c - 1
        variables.grid[i] = variables.symbol
        score = minimax(1, (-float('inf'), -float('inf')), (float('inf'), float('inf')))
        variables.grid[i] = c
        if score > max_score:
            max_score = score
            coordinate = c
    return coordinate
