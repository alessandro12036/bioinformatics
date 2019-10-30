def dna_complementer(string):
    r_string = string[::-1]
    result = ""
    for char in r_string:
        if char == "A":
            result += "T"
        elif char == "C":
            result += "G"
        elif char == "T":
            result += "A"
        else:
            result += "C"
    return result

if __name__ == "__main__":
    print(dna_complementer("AAAACCCGGT"))