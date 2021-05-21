s = [int(a) for a in input().split(" ")]
print(s[0] * s[1] if s[0] < 10 and s[1] < 10 else -1)
