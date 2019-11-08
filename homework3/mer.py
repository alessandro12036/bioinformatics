import os
import time
from utilities import file_reader

def merge_arrays2(a, b):
    start = time.time()
    i = j = 0
    sorted = []
    while len(a) > 0 and len(b) > 0:
        if a[i] < b[j]:
            sorted.append(a.pop(i))
        else:
            sorted.append(b.pop(i))
    if len(a) > 0:
        list_with_remaining = a
    else:
        list_with_remaining = b
    for el in list_with_remaining:
        sorted.append(el)
    print("Merge_arrays2 took {} seconds".format(time.time()-start))
    return sorted


def merge_arrays(a, b):
    i = j = 0
    sorted_arr = []
    counter = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sorted_arr.append(a[i])
            i += 1
        else:
            sorted_arr.append(b[j])
            j += 1
            counter += len(a) - i
    sorted_arr += a[i:] + b[j:]
    return counter, sorted_arr

if __name__ == "__main__":
    a = [2, 4, 10, 18]
    b = [-5, 11, 12]

    ls = file_reader("rosalind_mer.txt")
    a = list(map(int, ls[1].split()))
    b = list(map(int, ls[3].split()))
    n, ls = merge_arrays(a, b)
    s = " ".join(list(map(str, ls)))
    print(s)
