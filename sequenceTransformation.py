N, M = [int(x) for x in input().split()]
s = input()
longest = s
# -- loop start somewhere here
a, b, sp = input().split(";")
a = int(a)
b = int(b)
if a>b:
    temp = a
    a = b
    b = temp

new = s[:a]
new += sp
new += s[b+1:]
if len(new) > len(s):
    longest = new
s = new

print(s)
print(longest)