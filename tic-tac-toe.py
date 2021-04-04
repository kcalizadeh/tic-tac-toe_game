import re
import random

# a function for switching from player to player
def switch_player(active_player):
    if active_player == "X's Player":
        return "O's Player", 'O'
    else:
        return "X's Player", 'X'

# a function for asking if people want to play against computers or human opponents
def ask_opponent():
    while 0 == 0:
        request = input('Would you like to play against the computer (Y/N)? ')
        if request.lower() == 'y' or request.lower() == 'yes':
            opponent = 'computer'
            break
        if request.lower() == 'n' or request.lower() == 'no':
            opponent = 'human'
            break
        else:
            print('Please provide a valid input.')
    return opponent

# a function that enables users to choose which marker to use if they are playing
# against a computer (this also enables us to track who is the computer and who is
# the actual human player)
def choose_marker():
    while 0 == 0:
        choice = input('Would you like to use X or O? Please enter X or O. ')
        if choice.lower() == 'x':
            marker_choice = 'X'
            print(f"You have chosen to use X's. The computer will use O's.\n")
            break
        if choice.lower() == 'o':
            marker_choice = 'O'
            print(f"You have chosen to use O's. The computer will use X's.\n")
            break
        else:
            print('Please provide a valid input.')
    return marker_choice

# a function that takes user input and marks it on the grid
def make_move(active_player, grid, marker):
    while 0 == 0:
        move = input("\nEnter the number of the location you'd like to mark. ")
        # check if input is valid
        if move in grid:
            new_grid = re.sub(move, marker, grid)
            break
        else:
            print('Please provide a valid input.')
    return new_grid

# a function for the computer opponent to make moves
def make_computer_move(active_player, grid, marker):
    print(f"\nThe computer marked an {marker} on the grid.")
    while 0 == 0:
        # the computer makes moves at random
        move = str(random.randint(1,10))
        if move in grid:
            new_grid = re.sub(move, marker, grid)
            break
    return new_grid

# a function that checks if the game has been won
def check_winner(active_player, grid, marker):
    one = grid[1]
    two = grid[5]
    three = grid[9]
    four = grid[26]
    five = grid[30]
    six = grid[34]
    seven = grid[51]
    eight = grid[55]
    nine = grid[59]
    # going through the 8 ways the game can be won
    if one == marker and two == marker and three == marker:
        return 'winner detected'       
    if one == marker and five == marker and nine == marker:
        return 'winner detected'        
    if four == marker and five == marker and six == marker:
        return 'winner detected'        
    if seven == marker and eight == marker and nine == marker:
        return 'winner detected'       
    if seven == marker and five == marker and three == marker:
        return 'winner detected'       
    if one == marker and four == marker and seven == marker:
        return 'winner detected'       
    if two == marker and five == marker and eight == marker:
        return 'winner detected'  
    if three == marker and six == marker and nine == marker:
        return 'winner detected'
    else:
        return 0

# bringing it all together!
def run_game():
    # check what kind of opponent is desired
    opponent = ask_opponent()
    if opponent == 'computer':
        marker_choice = choose_marker()

    # this initializes the game and explains who goes first
    player_number = random.randint(1,2)
    if player_number == 1:
        player, marker = "X's Player", 'X'
    else:
        player, marker = "O's Player", 'O'
    grid = f' 1 | 2 | 3 \n ---------- \n 4 | 5 | 6 \n ---------- \n 7 | 8 | 9'
    print(f'The {player} will go first.')

    # here we make moves until a winner is detected or all the spaces have been used
    turn_count = 0
    winner = 0
    while winner == 0 and turn_count < 10:
        if opponent == 'computer' and marker != marker_choice:
            grid = make_computer_move(player, grid, marker)
        else:
            grid = make_move(player, grid, marker)
        winner = check_winner(player, grid, marker)
        if winner == 'winner detected':
            print(f'\nTHE {player.upper()} WINS!')
            if opponent == 'computer' and marker == marker_choice:
                print('Congratulations, you beat the computer.')
            print(f'\n{grid}')
            print('\nThe game has ended.')
            break
        player, marker = switch_player(player)
        turn_count += 1
        print(f'\n{grid}')
        if opponent == 'computer' and marker == marker_choice:
            print(f'\nYour turn.')
        else:
            print(f"\n{player}'s turn")
        if turn_count == 9:
            print("\nIt's a cat's game. \n      |\      _,,,---,,_\nZZZzz /,`.-'`'    -.  ,_``::,\n     |,4-  ) )-,_. ,\ (  `'-'\n    '---''(_/--'  `-'\_)")
            break
    again = input('Would you like to play again (Y/N)? ')
    if again.lower() == 'y' or again.lower() == 'yes':
        run_game()
    else:
        print('Thanks for playing, have a great day!')

# the game with a brief set of instructions for the first game
def present_and_run_game():
    print('Welcome to Terminal Tic-Tac-Toe!')
    print('In this game, you can play Tic-Tac-Toe in the terminal. The game grid looks like this:\n')
    print(f' 1 | 2 | 3 \n ---------- \n 4 | 5 | 6 \n ---------- \n 7 | 8 | 9')
    print('\nTo make a move, just enter the number of the space you want to mark. You may choose to play')
    print('against a human opponent or against the computer.\n\n')
    run_game()

present_and_run_game()