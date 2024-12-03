from random import randrange

# for i in range(10):
#     print(randrange(8))

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]
free_board_fields = []
game_continues = True
next_player_computer = True
have_winner = False

def print_welcome_message():
    print('=' * 25)
    print(' ' * 7 + 'TIC-TAC-TOE' + ' ' * 7)
    print('=' * 25)
    print()

def print_divider_line():
    print('+' + '-' * 7 + '+' + '-' * 7 + '+' + '-' * 7 + '+')

def print_empty_line():
    print('|' + ' ' * 7 + '|' + ' ' * 7 + '|' + ' ' * 7 + '|')

def print_board_row(row):
    print_divider_line()
    print_empty_line()
    print('|' + ' ' * 3 + row[0] +  ' ' * 3
          + '|' + ' ' * 3 + row[1] +  ' ' * 3
          + '|' + ' ' * 3 + row[2] +  ' ' * 3 + '|')
    print_empty_line()

def display_board():
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print_board_row(row)
    print_divider_line()

def make_list_of_free_fields():
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    if len(free_board_fields) != 0:
        free_board_fields.clear()
    for i, row in enumerate(board):
        for j, field in enumerate(row):
            if field not in ('X', 'O'):
                free_board_fields.append((i, j))
    print(f'Free fields: {free_board_fields}') # DEBUG: DELETE

def draw_computer_move():
    # The function draws the computer's move and updates the board.
    make_list_of_free_fields()
    print('\nIt\'s my turn. There you go.')
    move_index = randrange(len(free_board_fields))
    move = free_board_fields[move_index]
    move_row, move_column = move
    sign = 'X'
    board[move_row][move_column] = sign
    check_victory_for(sign)
    global next_player_computer
    next_player_computer = False

def enter_move():
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    make_list_of_free_fields()
    while True:
        print('\nYour turn.')
        try:
            move_row = int(input('Enter your row field (0, 1, 2): '))
            move_column = int(input('Enter your column field (0, 1, 2): '))
            break
        except ValueError:
            print('You entered an invalid value. Please try again.\n')
    sign = 'O'
    board[move_row][move_column] = sign
    check_victory_for(sign)
    global next_player_computer
    next_player_computer = True

def check_victory_for(sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    global have_winner
    global game_continues
    if board[0][0] == board[0][1] == board[0][2] \
        or board[1][0] == board[1][1] == board[1][2] \
        or board[2][0] == board[2][1] == board[2][2] \
        or board[0][0] == board[1][0] == board[2][0] \
        or board[0][1] == board[1][1] == board[2][1] \
        or board[0][2] == board[1][2] == board[2][2] \
        or board[0][0] == board[1][1] == board[2][2] \
        or board[0][2] == board[1][1] == board[2][0]:
        have_winner = True

    if have_winner:
        game_continues = False
        display_victory_message(sign)

def display_victory_message(sign):
    print('We have a winner!')
    if sign == 'X':
        print('Computer wins!')
    elif sign == 'O':
        print('Player wins!')

def main():
    print_welcome_message()
    while game_continues:
        display_board()
        if next_player_computer:
            draw_computer_move()
        else:
            enter_move()

main()
