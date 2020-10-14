import numpy

if __name__ == "__main__":
    l = input().split(' ')
    l = numpy.array(l, int)
    l = numpy.reshape(l, (3, 3))
    print(l)
