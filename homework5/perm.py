from itertools import permutations

def perm(n):
    l = range(1, n+1)
    perms = list(permutations(l))
    return len(perms), perms


if __name__ == "__main__":

    k = input("Insert number: ")
    length, p = perm(int(k))
    print(length)
    for x in p:
        print(" ".join(list(map(str, x))))