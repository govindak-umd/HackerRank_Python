#!/bin/python3

from datetime import datetime as dt
import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
        # t1 = t1[4:]
        # t2 = t2[4:]
        dt_object1 = dt.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
        # print("dt_object1 =", dt_object1)
        dt_object2 = dt.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
        # print("dt_object1 =", dt_object2)-
        print(int(abs(dt_object1-dt_object2).total_seconds()))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

    #     fptr.write(delta + '\n')

    # fptr.close()
