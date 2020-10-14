import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().split())
    main_mat = []
    for i in range(n):
        l = input().split()
        l = np.array(l, int)
        main_mat.append(l)
    main_mat = np.array(main_mat)
    sum = np.sum(main_mat, axis=0)
    prod = np.prod(sum)
    print(prod)
