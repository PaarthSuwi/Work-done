# Tic Tac Toe using indexing

# Create a 3x3 board
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Function to print the board
def print_board():
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if a player has won
def check_win(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    
    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    
    # Check diagonals
    if [board[i][i] for i in range(3)].count(player) == 3:
        return True
    if [board[i][2-i] for i in range(3)].count(player) == 3:
        return True
    
    return False

# Function to play the game
def play_game():
    player = 'X'
    while True:
        print_board()
        row = int(input('Enter the row (0-2): '))
        col = int(input('Enter the column (0-2): '))
        
        # Check if the chosen position is valid
        if board[row][col] != '-':
            print('Invalid move. Try again.')
            continue
        
        # Make the move
        board[row][col] = player
        
        # Check if the player has won
        if check_win(player):
            print_board()
            print(f'Player {player} wins!')
            break
        
        # Check if the board is full
        if all([cell != '-' for row in board for cell in row]):
            print_board()
            print('It\'s a tie!')
            break
        
        # Switch players
        player = 'O' if player == 'X' else 'X'

# Start the game
play_game()