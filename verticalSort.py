import copy

n, m = [int(x) for x in input().split()]
mat = []
for i in range(m):
    row = list(map(int, input().split()))
    mat.append(row)

result = copy.deepcopy(mat)
for i in range(m):
    for j in range(n):
        result[i][j] = 0

for j in range(n):
    current = []
    for i in range(m):
        current.append(mat[i][j])
    current = sorted(current)

    for i in range(m):
        result[i][j] = current[i]

for i in range(m):
    for j in range(n):
        print(result[i][j], end=" ")
    print()