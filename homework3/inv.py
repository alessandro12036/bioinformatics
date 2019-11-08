from utilities import file_reader
import time
from ms import merge_sort
import mer

def count_inv(arr):
    swaps, sorted_arr = merge_sort(arr)
    return sorted_arr, swaps


def count_inv2(arr):
    start = time.time()
    swaps = 0
    for i in range(len(arr)):
        smallest_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_i]:
                smallest_i = j
        if smallest_i != i:
            arr[i], arr[smallest_i] = arr[smallest_i], arr[i]
            swaps += 1
    print(time.time()-start)
    return swaps

if __name__ == "__main__":
    input_list = file_reader("rosalind_inv.txt")
    l = list(map(int, input_list[1].split()))
    l_sample = [-6, 1, 15, 8, 10]
    a, n = count_inv(l_sample)
    print(l_sample)
    print(n)
    a, n = count_inv(l)
    print(a)
    print(n)