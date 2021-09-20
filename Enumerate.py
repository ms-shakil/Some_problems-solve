board = [" " for _ in range(9)]
def available_move(board):
    move = [i for i,x in enumerate(board) if x == " "]
    return move

print(available_move(board))
print(board)
for i in enumerate(board):
    print(i)