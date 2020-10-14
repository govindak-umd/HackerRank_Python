def count_substring(string, sub_string):
    count = 0
    flag = True
    while (flag == True):
        a = string.find(sub_string)
        string = string[a + 1:]
        if a == -1:
            flag = False
        else:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
