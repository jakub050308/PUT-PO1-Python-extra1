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

