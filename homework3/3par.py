from utilities import file_reader

def par(arr):
    i = len(arr)-1
    pivot = arr[0]
    for j in range(len(arr)-1, 0, -1):
        if arr[j] > pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i -= 1
    arr[i], arr[0] = arr[0], arr[i]
    i -= 1
    for j in range(i, -1, -1):
        if arr[j] == pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i -= 1
    return arr

if __name__ == "__main__":
    input_list = file_reader("rosalind_par3.txt")
    sample = [4, 5, 6, 4, 1, 2, 5, 7, 4]
    array = list(map(int, input_list[1].split()))
    par(array)
    par(sample)
    print(sample)
    answer = " ".join(list(map(str, array)))
    print(answer)