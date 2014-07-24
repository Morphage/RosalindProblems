import itertools

def permutations(n):
    return list(itertools.permutations(range(1, n+1)))

if __name__ == '__main__':
    n = 3
    perms = permutations(n)
    print len(perms)

    for perm in permutations(n):
        for i in range(0, n):
            print perm[i], 
        print ""