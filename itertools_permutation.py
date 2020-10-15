from itertools import permutations

s = input().split()
l = []
for i in list(permutations(s[0], int(s[1]))):
    p = ''
    for chars in i:
        p = p + chars
    l.append(p)
l.sort()
for i in l:
    print(i)
