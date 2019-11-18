import os
from utilities import file_reader


def gc_counter(string):
    gc = 0
    for b in string:
        if b.lower() in "gc":
            gc += 1
    return gc / len(string)


if __name__ == "__main__":
    input_list = file_reader("rosalind_gc.txt", fasta=True)[1:]
    best_fasta = None
    best_count = 0
    for i in range(len(input_list)):
        input_sublist = input_list[i].split("\n")
        fasta_name = input_sublist[0]
        fasta_code = "".join(input_sublist[1:])
        c = gc_counter(fasta_code)
        if c > best_count:
            best_fasta = fasta_name
            best_count = c
    print(best_fasta)
    print(best_count*100)