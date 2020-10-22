from itertools import combinations
l = input().split(' ')
for i in range(0,int(l[1])):
    val_1 = list(combinations(sorted(l[0]),i+1))
    res = list(map("".join, val_1))
    # res.sort()
    for ans in res:
        print(ans)