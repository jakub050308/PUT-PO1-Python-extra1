def crossL(board, y, x):
    if x < 0:
        return
    else:
        if board[y][x] == 'o':
            board[y][x] = 'X'
        if board[y][x] == 'k':
            board[y][x] = 'M'
        crossL(board, y, x-1)
def crossR(board, y, x):
    if x >= 8:
        return
    else:
        if board[y][x] == 'o':
            board[y][x] = 'X'
        if board[y][x] == 'k':
            board[y][x] = 'M'
        crossR(board, y, x+1)

def crossU(board, y, x):
    if y<0:
        return
    else:
        if board[y][x] == 'o':
            board[y][x] = 'X'
        if board[y][x] == 'k':
            board[y][x] = 'M'
        crossU(board, y-1, x)

def crossD(board, y, x):
    if y>=8:
        return
    else:
        if board[y][x] == 'o':
            board[y][x] = 'X'
        if board[y][x] == 'k':
            board[y][x] = 'M'
        crossD(board, y+1, x)

# board[y][x]  !!!

board = []

for _ in range(8):
    board.append(list(map(str, input())))

#print(board[3][0])

for i in range(8):
    for j in range(8):
        if board[i][j] == 'w':
            crossD(board, i+1, j)
            crossU(board, i-1, j)
            crossL(board, i, j-1)
            crossR(board, i, j+1)

# for i in range(8):
#     for j in range(8):
#         print(board[i][j], end=" ")
#     print()

kingX = 0
kingY = 0

for i in range(8):
    for j in range(8):
        if board[i][j] == 'k' or board[i][j] == 'M':
            kingX = j
            kingY = i

# print(kingX)
# print(kingY)

if