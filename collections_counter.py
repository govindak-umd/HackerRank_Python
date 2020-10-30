from collections import Counter

n = int(input())
l = list(map(int, input().split()))
num_cust = int(input())
count = 0
d = Counter(l)
for i in range(num_cust):
    a, b = input().split()
    a = int(a)
    b = int(b)

    if d[a] != 0:
        count += b
        d[a] -= 1
    else:
        pass

print(count)
