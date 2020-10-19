n, m = input().split()
n = int(n)
m = int(m)
master_list = []
for i in range(n):
    init_list = input().split()
    l_new = [int(g) for g in init_list]
    master_list.append(l_new)
k = int(input())
master_list.sort(key=lambda test_list: test_list[k])

for i in master_list:
    print(*i)
