import sys
input = sys.stdin.readline
print = sys.stdout.write


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    if (board[0][0] == board[1][1] == board[2][2] or
            board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]

    return None


for i in range(int(input())):
    game_board = []
    for _ in range(3):
        game_board.append(list(input()))

    winner = check_winner(game_board)
    if winner:
        if winner == '.':
            print('DRAW\n')
        else:
            print(f"{winner}\n")
    else:
        print('DRAW\n')
