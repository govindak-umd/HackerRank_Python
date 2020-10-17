from collections import OrderedDict

n = int(input())
list_of_name = []
all_dic = OrderedDict()
for i in range(n):
    *name,price = input().split(' ')
    if len(name) == 1:
        if name[0] in all_dic:
            all_dic[name[0]] += int(price)
        else:
            all_dic[name[0]] = int(price)
    else:
        s=' '
        s = s.join(name)
        if s in all_dic:
            all_dic[s] += int(price)
        else:
            all_dic[s] = int(price)

for k,v in all_dic.items():
    print(k,v)