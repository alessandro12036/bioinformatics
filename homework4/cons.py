from utilities import file_reader
import numpy as np
import os

def cons(strings_list, save_file=False, file_name="answer.txt"):
    profile_matrix = []
    final_string = ""
    b_list = ["a", "c", "g", "t"]
    print(strings_list)
    for j in range(len(strings_list[0])):
        b_counts = [0, 0, 0, 0]  # A C G T
        for i in range(len(strings_list)):
            char = strings_list[i][j]
            char = char.lower()
            if char == "a":
                b_counts[0] += 1
            elif char == "c":
                b_counts[1] += 1
            elif char == "g":
                b_counts[2] += 1
            elif char == "t":
                b_counts[3] += 1
            else:
                print("character not recognised")
        final_string += b_list[np.argmax(np.array(b_counts))]
        profile_matrix.append(b_counts)
    profile_matrix_t = np.array(profile_matrix).transpose()
    print(final_string.upper())
    print(profile_matrix_t)

    if save_file:
        with open(os.path.expanduser("~/downloads/" + file_name), "w") as file:
            file.write(final_string.upper()+"\n")
        with open(os.path.expanduser("~/downloads/" + file_name), "a+") as file:
            for i in range(len(profile_matrix_t)):
                string = b_list[i].upper() + ": " + " ".join(list(map(str, profile_matrix_t[i]))) + "\n"
                assert len(profile_matrix_t[i]) == len(strings_list[0])
                file.write(string)


if __name__ == "__main__":
    input_sample_list = ["ATCCAGCT", "GGGCAACT", "ATGGATCT", "AAGCAACC", "TTGGAACT", "ATGCCATT", "ATGGCACT"]
    cons(input_sample_list, save_file=True, file_name="sample.txt")
    true_input = file_reader("rosalind_cons.txt", fasta=True)[1:]
    final_list = []
    for string in true_input:
        final_list.append("".join(string.split("\n")[1:]))
    cons(final_list, save_file=True)

