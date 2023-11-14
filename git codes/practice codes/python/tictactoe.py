board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
def print_board():
    for row in board:
        print(' | '.join(row))
        print('---------')
def check_win(player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    if [board[i][i] for i in range(3)].count(player) == 3:
        return True
    if [board[i][2-i] for i in range(3)].count(player) == 3:
        return True
    return False
def play_game():
    player = 'X'
    while True:
        print_board()
        row = int(input('Enter the row (0-2): '))
        col = int(input('Enter the column (0-2): '))
             
        if board[row][col] != '-':
            print('Invalid move. Try again.')
            continue

        board[row][col] = player

        if check_win(player):
            print_board()
            print(f'Player {player} wins!')
            break

        if all([cell != '-' for row in board for cell in row]):
            print_board()
            print('It\'s a tie!')
            break

        player = 'O' if player == 'X' else 'X'

play_game()
