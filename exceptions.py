n = int(input())
for i in range(n):
    a, b = input().split()
    try:
        a = int(a)
        b = int(b)
        res = a // b
        print(res)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except Exception as e:
        print("Error Code:", e)
