import re


def fun(s):
    count = 0
    # return True if s is a valid email, else return False
    r = re.split('@ |. |\@|\.', s)
    if len(r) == 3 and r[0]!='':
        # print('is factored rightly')
        count += 1
    else:
        return False
    if len(r[-1]) <= 3:
        # print('has correct extension')
        count += 1
    else:
        return False
    if r[1].isalnum():
        # print('website is alnum')
        count += 1
    else:
        return False
    for any_char in r[0]:
        if any_char.isalnum() or any_char == '_' or any_char == '-':
            # print('has correct starters')
            count += 1
    if count == 3 + len(r[0]):
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
