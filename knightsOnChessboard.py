def check(y, x):
    global board, n, count
    if y<0 or x<0 or y > n-1 or x > n-1:
        return
    else:
        if board[y][x] == 's':
            count += 1

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input())))
count = 0

for j in range(n):
    for i in range(n):
        if board[i][j] == 's':
            check(i-2, j-1)
            check(i-2, j+1)
            check(i-1, j-2)
            check(i-1, j+2)
            check(i+1, j-2)
            check(i+1, j+2)
            check(i+2, j-1)
            check(i+2, j+1)

print(count)