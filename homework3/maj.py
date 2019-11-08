from utilities import file_reader


def major_el(arr):
    best_count = 0
    best = None
    elements = set(arr)
    for el in elements:
        count = arr.count(el)
        if count > best_count:
            best = el
            best_count = count
    if best_count < len(arr) / 2:
        best = -1
    return best


if __name__ == "__main__":
    input_list = file_reader("rosalind_maj.txt")
    k, n = list(map(int, input_list[0].split()))
    results = []
    assert len(input_list[1:]) == k
    for i in range(1, k+1):
        array = list(map(int, input_list[i].split()))
        result = major_el(array)
        results.append(result)
    print(" ".join(list(map(str, results))))