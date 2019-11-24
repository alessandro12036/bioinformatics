from utilities import file_reader

def tran(stringA, stringB):
    transitions = 0
    traversions = 0
    for i in range(len(stringA)):
        b1 = stringA[i]
        b2 = stringB[i]
        if b1 != b2:
            if (b1 in "AG" and b2 in "AG") or (b1 in "CT" and b2 in "CT"):
                transitions += 1
            else:
                traversions += 1
    return transitions/traversions


if __name__ == "__main__":
    a = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
    b = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"
    print(tran(a, b))
    dataset = file_reader("rosalind_tran.txt", fasta=True)[1:]
    print(dataset)
    a = "".join(dataset[0].split("\n")[1:])
    b = "".join(dataset[1].split("\n")[1:])
    assert len(a) == len(b)
    print(tran(a, b))