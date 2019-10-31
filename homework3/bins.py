import os

def binary_search(l, to_find):
    start = 0
    end = len(l)-1
    while True:
        median = (start + end) // 2
        if start > end:
            return -1
        if to_find > l[median]:
            start = median + 1
        elif to_find < l[median]:
            end = median-1
        else:
            return median + 1


with open("./rosalind_bins.txt", "r") as file:
    input_list = file.read().split("\n")
    string, to_find_string = input_list[2], input_list[3]
l = list(map(int, string.split()))
to_find = list(map(int, to_find_string.split()))
for item in to_find:
    print(binary_search(l, item), end=" ")

