n = int(input())
word_dic = {}
for i in range(n):

    s = str(input())
    if s in word_dic.keys():
        word_dic[s] += 1
    else:
        word_dic[s] = 1

print(len(word_dic))
for k, v in word_dic.items():
    print(v, end=' ')
