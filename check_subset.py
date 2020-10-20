n = int(input())
for i in range(n):
    c = int(input())
    a = set(list(map(int, input().split(' ')[:c])))
    d = int(input())
    b = set(list(map(int, input().split(' ')[:d])))
    if a <= b:
        print('True')
    else:
        print('False')
