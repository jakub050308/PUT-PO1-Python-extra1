def check(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input()
palindrome = False
if check(s):
    palindrome = True

while palindrome == False:
    for i in range(len(s)):
        result = s[:i] + s[i+1::]
        if check(result):
            palindrome = True
            break
    break

while palindrome == False:
    pass
    # with 2 removed
    break

if palindrome:
    print("YES")
else:
    print("NO")