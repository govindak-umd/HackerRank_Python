def merge_the_tools(string, k):
    len_string = len(string)
    split_range = int(len_string / k)
    # print(len(string))
    all_strings = []
    for i in range(0, len_string, k):
        # print(i)
        all_strings.append(string[i:i + k])
    # print(all_strings)
    new_all_strings = []
    for every_string in all_strings:
        every_string = list(every_string)
        d = ''
        for i in every_string:
            if i not in d:
                d += i
        new_all_strings.append(d)
    for i in new_all_strings:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
