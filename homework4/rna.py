def dna_to_rna(string):
    return string.replace("T", "U")


if __name__ == "__main__":
    string = "GATGGAACTTGACTACGTAAATT"
    print(dna_to_rna(string))