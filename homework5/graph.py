from utilities import file_reader
import os

def graph(string_list, k=3):
    dict_1 = {}
    result = []
    names = []
    for string in string_list:
        sub_list = string.split("\n")
        name, s = sub_list[0], "".join(sub_list[1:])
        dict_1[name] = s
        names.append(name)
    for key1 in names:
        suffix = dict_1[key1][-k:]
        for key2 in names:
            if dict_1[key1] == dict_1[key2]:
                continue
            prefix = dict_1[key2][:k]
            if prefix == suffix:
                result.append(" ".join([key1, key2]))
    return result


if __name__ == "__main__":
    sample_string_list = [">Rosalind_0498\nAAATAAA",
                          ">Rosalind_2391\nAAATTTT",
                          ">Rosalind_2323\nTTTTCCC",
                          ">Rosalind_0442\nAAATCCC",
                          ">Rosalind_5013\nGGGTGGG"]
    print(graph(sample_string_list))
    dataset = file_reader("rosalind_grph.txt", fasta=True)[1:]
    with open(os.path.expanduser("~/downloads/answer.txt"), "w") as file:
        file.write("\n".join(graph(dataset)))