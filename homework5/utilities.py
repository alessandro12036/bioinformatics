import os
import time

def file_reader(file_name, fasta=False):
    to_split_at = "\n"
    if fasta:
        to_split_at = ">"
    path = os.path.expanduser("~/downloads/" + file_name)
    with open(path, "r") as file:
        s = file.read()
    return s.split(to_split_at)

# currently only works with one-argument functions
def timer(f):
    def wrapper(arg):
        start = time.time()
        r = f(arg)
        print(time.time()-start)
        return r
    return wrapper


RNA_TO_PROTEIN_DICT = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I",
                "GUC": "V", "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L",
                "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A", "UCC": "S",
                "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N",
                "GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q",
                "AAA": "K", "GAA": "E", "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C",
                "CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G", "UGG": "W", "CGG": "R", "AGG": "R",
                "GGG": "G"}

if __name__ == "__main__":
    l = file_reader("rosalind_3sum.txt")
    for el in l:
        print(el)
    print(len(l))
