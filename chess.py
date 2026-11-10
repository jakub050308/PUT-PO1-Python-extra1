def check(board, y, x):
    if x<0 or x>=8 or y<0 or y>=8:
        return True
    else:
        if board[y][x] == 'X' or board[y][x] == 'W':
            return True
        else:
            return False

def crossL(board, y, x):
    if x < 0:
        return
    else:
        if board[y][x] == 'o':
            board[y][x] = 'X'
        if board[y][x] == 'k':
            board[y][x] = 'M'
        if board[y][x] == 'w':
            board[y][x] = 'W'
        crossL(board, y, x-1)
def crossR(board, y, x):
    if x >= 8:
        return
    else:
        if board[y][x] == 'o':
            board[y][x] = 'X'
        if board[y][x] == 'k':
            board[y][x] = 'M'
        if board[y][x] == 'w':
            board[y][x] = 'W'
        crossR(board, y, x+1)

def crossU(board, y, x):
    if y<0:
        return
    else:
        if board[y][x] == 'o':
            board[y][x] = 'X'
        if board[y][x] == 'k':
            board[y][x] = 'M'
        if board[y][x] == 'w':
            board[y][x] = 'W'
        crossU(board, y-1, x)

def crossD(board, y, x):
    if y>=8:
        return
    else:
        if board[y][x] == 'o':
            board[y][x] = 'X'
        if board[y][x] == 'k':
            board[y][x] = 'M'
        if board[y][x] == 'w':
            board[y][x] = 'W'
        crossD(board, y+1, x)

# board[y][x]  !!!

board = []

for _ in range(8):
    board.append(list(map(str, input())))

#print(board[3][0])

for i in range(8):
    for j in range(8):
        if board[i][j] == 'w' or board[i][j] == 'W':
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

if check(board, kingY-1, kingX-1) and check(board, kingY-1, kingX) and check(board, kingY-1, kingX+1) and check(board, kingY, kingX-1) and check(board, kingY, kingX+1) and check(board, kingY+1, kingX-1) and check(board, kingY+1, kingX) and check(board, kingY+1, kingX+1):
    if board[kingY][kingX] == 'k':
        print("pat")
    elif board[kingY][kingX] == 'M':
        print("mat")
else:
    print("game goes on")