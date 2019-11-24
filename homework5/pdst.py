from utilities import file_reader


def pdst(l):
    matrix = []
    for el1 in l:
        row = []
        for el2 in l:
            counter = 0
            for i in range(len(el1)):
                if el1[i] != el2[i]:
                    counter += 1
            row.append(counter/len(el1))
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    sample_l = ["TTTCCATTTA", "GATTCATTTC", "TTTCCATTTT", "GTTCCATTTA"]
    m = pdst(sample_l)
    for row in m:
        print(" ".join(list(map(str, row))))

    dataset = file_reader("rosalind_pdst.txt", fasta=True)[1:]
    final_list = []
    for el in dataset:
        s = "".join(el.split("\n")[1:])
        final_list.append(s)
    m = pdst(final_list)
    for row in m:
        print(" ".join(list(map(str, row))))