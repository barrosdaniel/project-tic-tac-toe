from random import randrange

# for i in range(10):
#     print(randrange(8))

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]
free_board_fields = []

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
    for i in range(len(board)):
        for j in range(len(board[i])):
            field_value = board[i][j]
            if field_value != 'X' and field_value != 'O':
                free_board_fields.append((i, j))
                print(f'Free field found: row {i}, field {j}, value {field_value}')
    print(free_board_fields)


def draw_computer_move():
    # The function draws the computer's move and updates the board.
    make_list_of_free_fields()
    print('\nIt\'s my turn. There you go.')
    # TODO: Incomplete.

# def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

# def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game



def main():
    print_welcome_message()
    display_board()
    draw_computer_move()

main()
