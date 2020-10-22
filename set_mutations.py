n = int(input())
set_1 = set(list(map(int, input().split()[:n])))
m = int(input())
for i in range(m):
    l = input().split()
    set_sample = set(map(int, input().split()))
    if l[0] == 'intersection_update':
        set_1.intersection_update(set_sample)
    elif l[0] == 'update':
        set_1.update(set_sample)
    elif l[0] == 'symmetric_difference_update':
        set_1.symmetric_difference_update(set_sample)
    elif l[0] == 'difference_update':
        set_1.difference_update(set_sample)
print(sum(set_1))