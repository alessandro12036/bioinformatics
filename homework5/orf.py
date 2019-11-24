from utilities import file_reader
from prot import from_rna_to_protein
from rna import dna_to_rna
from revp import complementary_conv

START_CODON = "AUG"

def orf(s):
    r_s = complementary_conv(s[::-1])
    rna_s = dna_to_rna(s)
    rna_r_s = dna_to_rna(r_s)
    result = []
    for i in range(len(s)):
        if rna_s[i:i+3] == START_CODON:
            decoded = from_rna_to_protein(rna_s[i:])
            if decoded is not None:
                result.append(decoded)
        if rna_r_s[i:i+3] == START_CODON:
            decoded = from_rna_to_protein(rna_r_s[i:])
            if decoded is not None:
                result.append(decoded)
    return set(result)




if __name__ == "__main__":
    sample_string = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    print("\n".join(orf(sample_string)))
    print()
    dataset = file_reader("rosalind_orf.txt")
    string = "".join(dataset[1:])
    print("\n".join(orf(string)))
