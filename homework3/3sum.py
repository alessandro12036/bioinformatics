from utilities import file_reader
import time


def sum_3(a):
    dict_negatives = {}
    dict_positives = {}
    dict_zeros = {}
    length = len(a)
    for i in range(length):
        for j in range(i+1,len(a)):
            sum_ = a[i] + a[j]
            if sum_ < 0:
                dict_negatives[sum_] = (i, j)
            elif sum_ > 0:
                dict_positives[sum_] = (i, j)
            else:
                dict_zeros[sum_] = (i, j)
    for i in range(length):
        value = a[i]
        if value < 0:
            for j in dict_positives.keys():
                if j == -value and i not in dict_positives[j]:
                    index1, index2 = dict_positives[j]
                    return index1+1, index2+1, i+1
        elif value > 0:
            for j in dict_negatives.keys():
                if j == -value and i not in dict_negatives[j]:
                    index1, index2 = dict_negatives[j]
                    return index1+1, index2+1, i+1
        else:
            for j in dict_zeros.keys():
                if i not in dict_zeros[j]:
                    index1, index2 = dict_zeros[j]
                    return index1+1, index2+1, i+1
    else:
        return [-1]


l = file_reader("rosalind_3sum.txt")
k = l[0].split()[0]
results = []
input_sample = ["4 5", "2 -3 4 10 5", "8 -6 4 -2 -8", "-5 2 3 2 -4", "2 4 -5 6 8"]
k_sample = input_sample[0].split()[0]

# Sample test
for ind in range(1, int(k_sample)+1):
    result = sum_3(list(map(int, input_sample[ind].split())))
    print("{}: {}".format(input_sample[ind], sorted(result)))
print()

# True test
start = time.time()
for ind in range(1, int(k)+1):
    result = sum_3(list(map(int, l[ind].split())))
    print(" ".join(list(map(str, sorted(result)))))
print(time.time()-start)
