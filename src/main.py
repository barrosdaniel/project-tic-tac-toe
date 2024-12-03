"""
Tic-Tac-Toe Game

A simple implementation of the classic Tic-Tac-Toe game where a human player
competes against a computer opponent.

The game is played on a 3x3 grid where:
- The computer uses 'X' as its symbol
- The human player uses 'O' as their symbol
- Empty squares are numbered 1-9

Players take turns placing their symbols on the board until either:
- One player wins by getting 3 symbols in a row (horizontally, vertically or diagonally)
- The board is full with no winner (draw)

The computer makes random valid moves while the human player inputs their desired
position using row and column coordinates.

Functions:
    print_welcome_message(): Displays game title banner
    print_divider_line(): Prints horizontal board separator
    print_empty_line(): Prints empty line for board spacing
    print_board_row(row): Prints a single row of the game board
    display_board(): Shows current game board state
    make_list_of_free_fields(): Updates list of available board positions
    draw_computer_move(): Executes computer's turn
    enter_move(): Handles human player's turn
    check_victory_for(sign): Checks if given player has won
    display_victory_message(sign): Announces winner
    main(): Main game loop

Author: Daniel Barros
Version: 1.0
"""
from random import randrange

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]
free_board_fields = []
game_continues = True
next_player_computer = True
have_winner = False

def print_welcome_message():
    """
    Displays a welcome message banner for the Tic-Tac-Toe game.
    
    Prints a formatted title banner with the game name "TIC-TAC-TOE"
    centered between decorative equals signs.
    """
    print('=' * 25)
    print(' ' * 7 + 'TIC-TAC-TOE' + ' ' * 7)
    print('=' * 25)
    print()

def print_divider_line():
    """
    Prints a horizontal divider line used to separate rows in the game board.
    
    Creates a line using '+' for corners and '-' for horizontal segments.
    """
    print('+' + '-' * 7 + '+' + '-' * 7 + '+' + '-' * 7 + '+')

def print_empty_line():
    """
    Prints an empty line with vertical borders used for spacing in the game board.
    
    Creates a line using '|' for vertical borders with empty spaces between.
    """
    print('|' + ' ' * 7 + '|' + ' ' * 7 + '|' + ' ' * 7 + '|')

def print_board_row(row):
    """
    Prints a single row of the game board with the given row values.
    
    Args:
        row (list): A list containing 3 values representing one row of the board.
    """
    print_divider_line()
    print_empty_line()
    print('|' + ' ' * 3 + row[0] +  ' ' * 3
          + '|' + ' ' * 3 + row[1] +  ' ' * 3
          + '|' + ' ' * 3 + row[2] +  ' ' * 3 + '|')
    print_empty_line()

def display_board():
    """
    Displays the current state of the game board.
    
    Prints the complete game board by iterating through each row and displaying
    the values with appropriate formatting and borders.
    """
    for row in board:
        print_board_row(row)
    print_divider_line()

def make_list_of_free_fields():
    """
    Creates a list of all available positions on the game board.
    
    Scans the board and adds the coordinates of empty squares to the 
    free_board_fields list. The list is updated with the available positions as tuples of
    (row, column). Clears any existing entries before scanning.
    """
    if len(free_board_fields) != 0:
        free_board_fields.clear()
    for i, row in enumerate(board):
        for j, field in enumerate(row):
            if field not in ('X', 'O'):
                free_board_fields.append((i, j))

def draw_computer_move():
    """
    Executes the computer's turn in the game.
    
    Randomly selects an available position from free_board_fields,
    places an 'X' at that position, and checks if the move resulted in a win.
    Updates next_player_computer to False after the move, so that the next move
    is performed by a player.
    """
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
    """
    Handles the human player's turn in the game.
    
    Prompts the player to enter row and column coordinates for their move,
    validates the input, places an 'O' at the chosen position, and checks for a win.
    Updates next_player_computer to True after the move, so that the next move is
    performed by the computer.
    """
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
    """
    Checks if the given player has won the game.
    
    Examines all possible winning combinations (rows, columns and diagonals)
    to determine if the player with the given sign has achieved victory.
    Updates game state variables if a winner is found.

    Args:
        sign (str): The player's symbol ('X' for computer or 'O' for human)
    
    Global variables modified:
        have_winner: Set to True if a winning combination is found
        game_continues: Set to False if a winner is determined
    """
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
    """
    Displays the victory message announcing the winner of the game.
    
    Prints a message indicating that there is a winner and specifies whether
    the computer ('X') or human player ('O') has won.

    Args:
        sign (str): The symbol of the winning player ('X' for computer, 'O' for human)
    """
    print('We have a winner!')
    if sign == 'X':
        print('Computer wins!')
    elif sign == 'O':
        print('Player wins!')

def main():
    """
    Main game loop that controls the flow of the Tic-Tac-Toe game.

    Initialises the game by displaying the welcome message and enters the main game loop.
    The loop continues until there is a winner or the board is full (draw).
    In each iteration:
    - Displays the current board state
    - Alternates turns between computer and human player based on next_player_computer flag
    - Computer makes random valid moves when it's their turn
    - Human player enters row/column coordinates on their turn
    - Checks for victory conditions after each move

    The game ends when either:
    - One player gets three symbols in a row (horizontally, vertically or diagonally)
    - The board is full with no winner (draw)
    """
    print_welcome_message()
    while game_continues:
        display_board()
        if next_player_computer:
            draw_computer_move()
        else:
            enter_move()

main()
