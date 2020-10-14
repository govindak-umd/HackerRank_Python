def validate(name):
    flag_count = 0

    if len(name) == 10:
        flag_count += 1

    name_list = list(name)
    name_set = set(name_list)
    if len(name_set) == len(name_list):
        flag_count += 1

    if name.isalnum():
        flag_count += 1

    num_list = []
    for char in name:
        if char.isnumeric():
            num_list.append(char)
    if len(num_list) >= 3:
        flag_count += 1

    upper_list = []
    for char in name:
        if char.isupper():
            upper_list.append(char)
    if len(upper_list) >= 2:
        flag_count += 1

    if flag_count == 5:
        print("Valid")
    else:
        print("Invalid")


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        uid = str(input())
        validate(uid)
