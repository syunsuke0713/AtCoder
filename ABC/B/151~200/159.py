s = input()

n = len(s)
s1 = s[:n//2]
s2 = s[(n+2)//2:]
if s == s[::-1] and s1 == s1[::-1] and s2 == s2[::-1]:
    print("Yes")
else:
    print("No")