def permutations(x,y,z):
    perms = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) ]
    return(perms)

def extractElements(permutation, n):
    extracted_perms = [i for i in permutation if sum(i) != n]
    print(extracted_perms)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    all_permutations = permutations(x,y,z)
    #print(all_permutations)
    extractElements(all_permutations, n)

