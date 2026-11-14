def chckAvg(y, x):
    global n, room, result
    count = -1
    cmp = room[y][x]  #y = 0 x = 2
    summ = cmp * -1
    for k in range(n):
        if room[y][k] >= cmp:
            summ += room[y][k]
            count += 1
        if room[k][x] >= cmp:
            summ += room[k][x]
            count += 1

    #print(x, y, room[y][x], summ / count)
    if summ / count >= 7:
        return True
    else:
        return False

n = int(input())
room = []

for _ in range(n):
    room.append(list(map(int, input().split())))

result = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    result.append(row)

for j in range(n):
    for i in range(n):
        if room[i][j] >= 7:
            result[i][j] = 1
            #print('s')
        elif chckAvg(i, j):
            result[i][j] = 1

for j in range(n):
    for i in range(n):
        print(result[j][i], end=" ")
    print()