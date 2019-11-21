from utilities import file_reader, timer


def complementary_conv(to_convert):
    converted = ""
    for b in to_convert:
        if b == "A":
            converted += "T"
        elif b == "T":
            converted += "A"
        elif b == "G":
            converted += "C"
        elif b == "C":
            converted += "G"
        else:
            raise ValueError("Character not recognized")
    return converted


@timer
def revp(string):
    string = string.upper()
    c_string = complementary_conv(string)
    result = []
    for i in range(len(string)-1):
        for j in range(i+2, len(string)):
            if string[i:j] == c_string[j:i:-1]:
                result.append((i+1, len(string[i:j])+1))
    return result


if __name__ == "__main__":
    sample_string = "TCAATGCATGCGGGTCTATATGCAT"
    r = revp(sample_string)
    for i, length in r:
        print(i, length)
    true_dataset = file_reader("rosalind_revp.txt", fasta=True)[1]
    processed_dataset = true_dataset.split("\n")
    fasta_name, actual_string = processed_dataset[0], "".join(processed_dataset[1:])
    for i, length in revp(actual_string):
        print(i, length)
