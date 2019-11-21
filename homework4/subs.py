from utilities import file_reader

def find_motif(string, substring):
    i = 0
    indices = []
    while len(string[i:]) > len(substring):
        index = string.find(substring, i)
        if index >= 0:
            indices.append(index+1)
            i = index + 1
        else:
            break
    return indices


if __name__ == "__main__":
    sample_string = "GATATATGCATATACTT"
    sample_substring = "ATAT"
    print(find_motif(sample_string, sample_substring))
    true_dataset = file_reader("rosalind_subs.txt")
    print(true_dataset)
    string, substring, _ = true_dataset
    print(" ".join(list(map(str, find_motif(string, substring)))))