n = int(input())
l = input().split(' ')

print(all([int(i)>0 for i in l]) and any([k == k[::-1] for k in l]))