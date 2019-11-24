from utilities import file_reader


def sseq(s, t):
    i_t = 0
    indices = []
    for i in range(len(s)):
        if s[i] == t[i_t]:
            i_t += 1
            indices.append(i+1)
        if i_t >= len(t):
            break
    return indices


if __name__ == "__main__":
    sample_string = "ACGTACGTGACG"
    sample_seq = "GTA"
    print((sseq(sample_string, sample_seq)))
    not_splitted_string, not_splitted_seq = file_reader("rosalind_sseq.txt", fasta=True)[1:]
    string = "".join(not_splitted_string.split("\n")[1:])
    seq = not_splitted_seq.split("\n")[1]
    r = list(map(str, sseq(string, seq)))
    print(" ".join(r))