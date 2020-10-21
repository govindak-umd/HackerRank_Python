import numpy as np
n = int(input())
l = []
for i in range(n):
    c = list(map(float,input().split()))
    # print(c)
    l.append(c)
print (round((np.linalg.det(l)),2))