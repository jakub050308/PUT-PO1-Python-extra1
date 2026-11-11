def checkSurround(x, y, room):
    sum = 0
    sum += numbers(x - 1, y, room)
    sum += numbers(x + 1, y, room)
    sum += numbers(x, y - 1, room)
    sum += numbers(x, y + 1, room)
    sum += numbers(x - 1, y - 1, room)
    sum += numbers(x - 1, y + 1, room)
    sum += numbers(x + 1, y - 1, room)
    sum += numbers(x + 1, y + 1, room)
    return sum


def numbers(x, y, room):
    if x<0 or y<0 or x>n-1 or y > n-1:
        return 0
    else:
        return room[y][x]

def check(room, x, y, result):
    global n
    if room[y][x] >= 3:
        result[y][x] = 1
        return
    elif x == 0 and y == 0 or x == 0 and y == n-1 or x == n-1 and y == 0 or x == n-1 and y == n-1:
        count = 3
        sum = checkSurround(x, y, room)
        avg = sum / count
        if avg >= 3:
            result[y][x] = 1
            return
    elif x == 0 or y == 0 or x == n-1 or y == n-1:
        count = 5
        sum = checkSurround(x, y, room)
        avg = sum / count
        if avg >= 3:
            result[y][x] = 1
            return
    else:
        count = 8
        sum = checkSurround(x, y, room)
        avg = sum/ count
        if avg >= 3:
            result[y][x] = 1
        return

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
        check(room, i, j, result)

for j in range(n):
    for i in range(n):
        print(result[j][i], end=" ")
    print()