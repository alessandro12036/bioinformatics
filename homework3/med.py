from utilities import file_reader


def med(arr, kth):
    for _ in range(kth - 1):
        arr.remove(min(arr))
    return min(arr)


if __name__ == "__main__":
    input_list = file_reader("rosalind_med.txt")
    sample = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
    k_sample = 8
    print(med(sample, k_sample))
    array = list(map(int, input_list[1].split()))
    k = int(input_list[2])
    print(med(array, k))
