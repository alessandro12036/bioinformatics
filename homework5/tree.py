from utilities import file_reader


def tree(n, l):
    for i in range(len(l)):
        if len(l[i].split()) < 2:
            print("Singleton element found: ", l[i])
            l.pop(i)
    return n - 1 - len(l)


if __name__ == "__main__":
    l_sample = [("1 2"), ("2 8"), ("4 10"), ("5 9"), ("6, 10"), ("7 9"), ("3")]
    n_sample = 10
    print(tree(n_sample, l_sample))
    dataset = file_reader("rosalind_tree.txt")[:-1]
    print(dataset)
    n = int(dataset[0])
    l = dataset[1:]
    print(tree(n, l))