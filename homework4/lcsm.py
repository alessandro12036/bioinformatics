from utilities import file_reader


def lcsm(strings_list):
    ref_string = strings_list[0]
    max_found = ""
    for i in range(len(ref_string)):
        for j in range(i+1, len(ref_string)):
            found = True
            subsequence = ref_string[i:j]
            for string in strings_list[1:]:
                if subsequence not in string:
                    found = False
            if found:
                if len(subsequence) > len(max_found):
                    max_found = subsequence
            else:
                break
    return max_found


if __name__ == "__main__":

    sample_strings = ["GATTACA", "TAGACCA", "ATACA"]
    print(lcsm(sample_strings))
    true_input = file_reader("rosalind_lcsm.txt", fasta=True)[1:]
    final_list = []
    for input_ in true_input:
       sub_list = input_.split("\n")[1:]
       final_list.append("".join(sub_list))
    print(lcsm(final_list))