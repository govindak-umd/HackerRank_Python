if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr = list(arr)
    list_arr.sort()
    l = list(set(list_arr))
    l.sort()
    print(l[-2])
