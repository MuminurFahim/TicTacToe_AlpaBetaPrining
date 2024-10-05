import variables
import turns_func


def update_grid():
    print(f' {variables.grid[0]} | {variables.grid[1]} | {variables.grid[2]} \n'
          f'---+---+---\n'
          f' {variables.grid[3]} | {variables.grid[4]} | {variables.grid[5]} \n'
          f'---+---+---\n'
          f' {variables.grid[6]} | {variables.grid[7]} | {variables.grid[8]} \n')


def correct_input(message, lst):
    i = int(input(f'{message}: '))
    if i not in lst:
        print(f'input error: input is not valid. valid inputs: {lst}')
        return correct_input(message, lst)
    return i


def initialization():
    option = correct_input(variables.initialization_message, variables.valid_initials)
    if option in {1, 4, 5}:
        variables.turn = 'H'
    else:
        variables.turn = 'C'
    if option in {2, 4}:
        variables.difficulty = 'R'
    if option in {3, 5}:
        variables.difficulty = 'P'
    print('Coordinates of the grid:')
    update_grid()


def check_win():
    for x, y, z in (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6):
        if variables.grid[x] == variables.grid[y] == variables.grid[z]:
            return True
    return False


def availables():
    availables = []
    for c in variables.grid:
        if c not in variables.valid_symbols:
            availables.append(c)
    return availables


def get_coordinate():
    if not variables.difficulty:
        return turns_func.human_turn()
    elif variables.turn == 'H':
        variables.turn = 'C'
        return turns_func.human_turn()
    else:
        print(f'computer ({variables.symbol}):')
        variables.turn = 'H'
        if variables.difficulty == 'R':
            return turns_func.random_turn()
        else:
            return turns_func.perfect_turn()


def play():
    coordinate = get_coordinate()
    variables.grid[coordinate - 1] = variables.symbol
    update_grid()
    variables.moves += 1
    if check_win():
        print(f'"{variables.symbol}" wins in {variables.moves} moves!')
    elif not availables():
        print('"Game Ties"')
    else:
        changed = variables.valid_symbols - {variables.symbol}
        variables.symbol = changed.pop()
        play()
