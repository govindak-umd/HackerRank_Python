n, k = input().split()
k = int(k)
s = input()
polynomial = ''
for i in s:
    if i == 'x':
        i = str(n)
        polynomial += i
    else:
        polynomial += i
if int(eval(polynomial)) == k:
    print('True')
else:
    print('False')
