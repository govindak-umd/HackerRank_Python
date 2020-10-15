from itertools import permutations
import itertools

k, m = input().split()
k = int(k)
all_inputs = []
for i in range(k):
    N = [int(x) ** 2 for x in input().split()]
    all_inputs.append(N)
for i in all_inputs:
    for val in range(len(i)):
        i[val] = int(i[val])


# print(all_inputs)


def maximize(list_input, m):
    all_combo_list = list(itertools.product(*list_input))
    ans = 0
    for i in all_combo_list:
        maxim = 0
        for every_num in i:
            maxim += every_num
        maxim = maxim % m
        if maxim > ans:
            ans = maxim
    print(ans)


new_input = []
for i in all_inputs:
    new_input.append(i[1:])
# print(new_input)
m = int(m)
maximize(new_input, m)
