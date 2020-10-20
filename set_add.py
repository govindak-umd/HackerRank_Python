n = int(input())
l = []
for i in range(n):
    inp = str(input())
    l.append(inp)
l = list(set(l))
print(len(l ))
