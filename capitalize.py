#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    dic = {}
    for i in range(len(s)):
        dic[i] = s[i]
        if (s[i - 1] == " " and s[i - 1 != " "] and i != 0):
            dic[i] = s[i].upper()
        if i == 0 and i != " ":
            dic[i] = s[i].upper()
    print(dic)
    new = ''
    for k, v in dic.items():
        new += v
    return new


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
