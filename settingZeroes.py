import copy
def zeroR(par, lim):
    global result
    for v in range(lim):
        result[par][v] = 0

def zeroC(par, lim):
    global result
    for v in range(lim):
        result[v][par] = 0

N, M = [int(x) for x in input().split()]
# print(N, M)
mat = []
result = []
for _ in range(N):
    row = list(map(int, input().split()))
    # print(row)
    mat.append(row)

result = copy.deepcopy(mat)

for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            zeroR(i, M)
            zeroC(j, N)


for i in range(N):
    for j in range(M):
        print(result[i][j], end=" ")
    print()
