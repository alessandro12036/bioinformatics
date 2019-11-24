from utilities import file_reader
import numpy as np

def length_lcs(aString, bString):
    total_length = 0
    if len(aString) != 0 and len(bString) != 0:
        if aString[-1] == bString[-1]:
            total_length = lcsq(aString[:-1], bString[:-1])
            total_length += 1
        else:
            total_length = max(lcsq(aString[:-1], bString), lcsq(aString, bString[:-1]))
    return total_length


def matrix_decoder(m, s1):
    rows, columns = m.shape
    final_string = ""
    i = rows-1
    j = columns-1
    while i >= 0 and j >= 0:
        element = m[i, j]
        if element > m[i-1, j] and element > m[i, j-1]:
            final_string = s1[i-1] + final_string
            i -= 1
            j -= 1
        elif m[i-1, j] > m[i, j-1]:
            i -= 1
        else:
            j -= 1
    return final_string


def lcsq(s1, s2):
    rows, columns = len(s1)+1, len(s2)+1
    m = np.zeros((rows, columns))
    for i in range(1, rows):
        for j in range(1, columns):
            if s1[i-1] == s2[j-1]:
                m[i, j] = 1 + m[i-1, j-1]
            else:
                m[i, j] = max(m[i-1, j], m[i, j-1])
    return matrix_decoder(m, s1)


if __name__ == "__main__":
    string1_sample = "GXTXAYB"
    string2_sample = "AGGTAB"
    print(length_lcs(string1_sample, string2_sample))

    dataset = file_reader("rosalind_lcsq.txt", fasta=True)[1:]
    string1 = "".join(dataset[0].split("\n")[1:])
    string2 = "".join(dataset[1].split("\n")[1:])
    new_r = lcsq(string1, string2)
    print(lcsq(string1_sample, string2_sample))
    print(new_r)
