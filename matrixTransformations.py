def trans(m,n):
    global mat
    new = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(mat[j][i])
        new.append(row)
    mat = new

def revR(l, val):
    global mat
    temp = []
    for i in range(val):
        temp.append(mat[l][i])
    temp = temp[::-1]
    for i in range(val):
        mat[l][i] = temp[i]

def revC(l, val):
    global mat
    temp = []
    for i in range(val):
        temp.append(mat[i][l])
    temp = temp[::-1]
    for i in range(val):
        mat[i][l] = temp[i]


m, n = [int(x) for x in input().split()]
mat = []
for _ in range(m):  #    n?
    row = list(map(int, input().split()))
    mat.append(row)

k = int(input())
operations = []
indices = []

for _ in range(k):
    ans = input()
    if ans[0] == 'T':
        operations.append('T')
        indices.append(-1)
        break
    else:
        o, i = ans.split()
        operations.append(o)
        indices.append(int(i))
