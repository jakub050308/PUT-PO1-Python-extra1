def check(m):
    for i in range(9):
        zb = set()
        for j in range(9):
            zb.add(m[i][j])
        if len(zb) != 9:
            return False

    for i in range(9):
        zb = set()
        for j in range(9):
            zb.add(m[j][i])
        if len(zb) != 9:
            return False

    return True


def rdiag(m):
    zb = set()
    for i in range(9):
        zb.add(m[i][8-i])
    if len(zb) != 9:
        return False
    return True


def ldiag(m):
    zb = set()
    for i in range(9):
        zb.add(m[i][i])

    if len(zb) != 9:
        return False
    return True

m = []

for _ in range(9):
    row = list(map(int, input().split()))
    m.append(row)

if check(m):
    if ldiag(m) and rdiag(m):
        print('X')
    else:
        print(True)
else:
    print(False)