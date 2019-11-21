from rna import dna_to_rna
from utilities import file_reader, RNA_TO_PROTEIN_DICT

def splc(string, substrings_list):
    original_string = string
    processed_string = ""
    for substring in substrings_list:
        j = string.find(substring)
        if j > -1:
            processed_string = string[:j]
            processed_string += string[j+len(substring):]
            string = processed_string
    return processed_string


def from_rna_to_protein(string):
    codified = ""
    for i in range(0, len(string), 3):
        value_to_add = RNA_TO_PROTEIN_DICT[string[i:i+3]]
        if value_to_add != "Stop":
            codified += value_to_add
    return codified


if __name__ == "__main__":
    p_string = splc("ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG",
                    ["ATCGGTCGAA", "ATCGGTCGAGCGTGT"])
    rna_string = dna_to_rna(p_string)
    print(from_rna_to_protein(rna_string))
    true_dataset = file_reader("rosalind_splc.txt", fasta=True)[1:]
    substrings = []
    string = "".join(true_dataset[0].split("\n")[1:])
    for s in true_dataset[1:]:
        lines = s.split("\n")[:-1]
        substrings.append(lines[1])
    p_string = splc(string, substrings)
    rna_string = dna_to_rna(p_string)
    print(from_rna_to_protein(rna_string))
