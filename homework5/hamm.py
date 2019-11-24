from utilities import file_reader


def hamm_dist(a, b):
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1
    return counter


if __name__ == "__main__":

    string_a, string_b = file_reader("rosalind_hamm.txt")
    string_a_sample = "GAGCCTACTAACGGGAT"
    string_b_sample = "CATCGTAATGACGGCCT"
    print(hamm_dist(string_a_sample, string_b_sample))
    print("Now the true dataset:")
    print(hamm_dist(string_a, string_b))