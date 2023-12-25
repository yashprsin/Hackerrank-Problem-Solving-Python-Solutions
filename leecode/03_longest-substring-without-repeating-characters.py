s = "abcabcbb"
count = 0
n = int(len(s))
res = 0
for i in range(n):
    so = s[i:]
    if so in s:
        res += 1
    print(res)
