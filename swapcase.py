def swap_case(s):
    l = []
    for i in s:
        l.append(i)
    e = ""
    for i in l:
        if i.isupper():
            e += i.lower()
        elif i.islower():
            e += i.upper()
        else:
            e += i
    return e


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
