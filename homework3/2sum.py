from utilities import file_reader


def sum_(a):
    indices = []
    length = len(a)
    for i in range(length):
        for j in range(i+1,length):
            if int(a[i]) + int(a[j]) == 0:
                indices.append(str(i+1))
                indices.append(str(j+1))
                return indices
    return ["-1"]


l = file_reader("rosalind_2sum.txt")
k = l[0].split()[0]
results = []
for ind in range(int(k)):
    result = sum_(l[ind+1].split())
    print(" ".join(result))


