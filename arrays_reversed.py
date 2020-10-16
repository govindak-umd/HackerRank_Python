import numpy


def arrays(input_array):
    input_array = numpy.array(arr, float)
    reversed_arr = input_array[::-1]
    return reversed_arr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
