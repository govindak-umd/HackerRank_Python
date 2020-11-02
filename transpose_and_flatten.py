import numpy as np

N, M = input().split()
N = int(N)
M = int(M)
d = []
for i in range(N):
    c = list(map(int, input().split()))
    # print(c)
    d.insert(i, c)
arr = np.array(d)
print(arr.T)
# print(d)
print(arr.flatten())