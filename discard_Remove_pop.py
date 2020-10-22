n = int(input())
s =  set(list(map(int, input().split()[:n])))
# print(s)
comm = int(input())
for i in range(comm):
    l = input().split(' ')
    if l[0] == 'pop':
        s.pop()
        # print(s)
    if l[0] == 'remove':
        s.remove(int(l[1]))
        # print(s)
    elif l[0] == 'discard':
        s.discard(int(l[1]))
        # print(s)
print(sum(s))

