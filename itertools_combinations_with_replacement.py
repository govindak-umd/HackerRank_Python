from itertools import combinations_with_replacement
l = input().split(' ')
# for i in range(0,int(l[1])):
val_1 = list(combinations_with_replacement(sorted(l[0]),int(l[1])))
res = list(map("".join, val_1))
# res.sort()
for ans in res:
    print(ans)