from itertools import combinations
n = int(input())
c = input().split()
l = []
l_i = []
for i in range(len(c)):
    l_i.append(i+1)
    if c[i]=='a':
        l.append(i+1)
d = int(input())
val_1 = list(combinations(l_i,d))
# print(val_1)
final_l = []
for i in val_1:
    for j in l:
        if j in i:
            final_l.append(i)
final_l = list(set(final_l))
print(len(final_l)/len(val_1))