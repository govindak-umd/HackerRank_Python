n = int(input())
for i in range(n):
    mob = str(input())
    if len(mob) == 10:
        if mob[0] == '7' or mob[0] == '8' or mob[0] == '9':
            if mob.isdigit():
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
