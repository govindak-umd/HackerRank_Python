#!/bin/python3
import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string_list = []
for column_idx in range(m):
    s = ""
    for i in matrix:
        s += i[column_idx]
    string_list.append(s)
res = ''
for i in string_list:
    res += i

pattern = r'([A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])'
text = re.sub(pattern, r'\1 ', res)
print(text)
