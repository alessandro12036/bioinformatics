from utilities import file_reader
from itertools import product
import os

def lexf(string, k=2):
    string = "".join(string.split())
    solution = product(string, repeat=k)
    return solution


if __name__ == "__main__":
    sample_string = "A C G T"
    for a, b in lexf(sample_string):
        print(a, b)
    true_string, k = file_reader("rosalind_lexf.txt")[:-1]
    k = int(k)
    final_string = ""
    for l in lexf(true_string, k):
        final_string += "".join(l) + "\n"
    with open(os.path.expanduser("~/downloads/answer.txt"), "w") as file:
        file.write(final_string)
    print(final_string)
