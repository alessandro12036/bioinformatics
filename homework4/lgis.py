from utilities import file_reader
import numpy as np

def lgs(l, mode="increasing"):
    int_l = list(map(int, l))
    i = 1
    indices = [None] * len(int_l)
    lengths = [1] * len(int_l)
    condition_met = False
    while i < len(int_l):
        j = 0
        while j < i:
            if mode == "increasing":
                condition_met = int_l[j] < int_l[i]
            elif mode == "decreasing":
                condition_met = int_l[j] > int_l[i]
            if condition_met:
                if lengths[i] <= lengths[j]+1:
                    lengths[i] = lengths[j]+1
                    indices[i] = j
            j += 1
        i += 1
    i = int(np.argmax(lengths))
    result = [int_l[i]]
    while indices[i] != None:
        idx = indices[i]
        result.insert(0, int_l[idx])
        i = idx
    return list(map(str, result))


if __name__ == "__main__":
    a = "5 1 4 2 3"
    print(lgs(a.split(), mode="increasing"))
    print(lgs(a.split(), mode="decreasing"))
    total_input = file_reader("rosalind_lgis.txt")
    true_test = total_input[1].split()
    print(" ".join(lgs(true_test, mode="increasing")))
    print(" ".join(lgs(true_test, mode="decreasing")))
