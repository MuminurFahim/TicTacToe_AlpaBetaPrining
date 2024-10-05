initialization_message = ('1. Play with Human\n'
                          'Play with computer:\n'
                          'For computer going first, Difficulties:\n'
                          '\t2. Random\n'
                          '\t3. Perfect\n'
                          'For computer going second, Difficulties:\n'
                          '\t4. Random\n'
                          '\t5. Perfect\n'
                          'Choose an option. Enter the number')

get_coordinate_message = 'Input a coordinate for '

valid_initials = (1, 2, 3, 4, 5)
grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valid_symbols = {'X', 'O'}
symbol = 'X'
difficulty = None
turn = None
moves = 0
states = {}