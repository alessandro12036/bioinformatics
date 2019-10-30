def base_counter(string):
    a = string.count("A")
    c = string.count("C")
    g = string.count("G")
    t = string.count("T")
    result_string = str(a) + " " + str(c) + " " + str(g) + " " + str(t)
    return result_string


if __name__ == "__main__":
    string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    print(base_counter(string))