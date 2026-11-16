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
    for i in range(len(s)):
        for j in range(len(s)):
            if abs(i-j) <= 1:
                result = s[:min(i,j)] + s[max(i,j)+1::]
            else:
                result = s[:min(i,j)] + s[min(i,j)+1:max(i,j)] + s[max(i,j)+1::]

            if check(result):
                palindrome = True
                break
        if palindrome:
            break
    break

if palindrome:
    print("YES")
else:
    print("NO")