a,b = map(int,input().split())
l = list(map(int,input().split(' ')))
set_list = set(l)
set_1= set()
sum_val = 0
set_1 =  set(list(map(int, input().split(' ')[:a])))
set_2  = set()
set_2 =  set(list(map(int, input().split(' ')[:b])))
for val in set_list:
    if val in set_1:
        sum_val+=1
    elif val in set_2:
        sum_val-=1
print(sum_val)