if __name__ == '__main__':
    N = int(input())
    list_sample = []
    for i in range(N):
        l = []
        l = input().split()
        method = l[0]
        if len(l) == 2:
            val = int(l[1])
        if len(l) == 3:
            val = int(l[1])
            val2 = int(l[2])
        if method == 'insert':
            list_sample.insert(val, val2)
        if method == 'print':
            print(list_sample)
        if method == 'remove':
            list_sample.remove(val)
        if method == 'append':
            list_sample.append(val)
        if method == 'sort':
            list_sample.sort()
        if method == 'pop':
            list_sample.pop()
        if method == 'reverse':
            list_sample.reverse()
