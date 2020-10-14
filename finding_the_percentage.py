if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = student_marks[query_name]
    sum_l = 0
    for i in l:
        sum_l += i
    d = sum_l / (len(l))
    print("{0:.2f}".format(d))
