import textwrap


def wrap(string, max_width):
    i = ""
    for c in range(0, len(string), max_width):
        i += string[c:c + max_width] + "\n"
    return i


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
