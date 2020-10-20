n = int(input())
a = set()
a =  set(list(map(int, input().split(' ')[:n])))
b = set()
m = int(input())
b = set(list(map(int, input().split(' ')[:m])))
c = sorted(a.symmetric_difference(b))
for i in c:
    print(i)

