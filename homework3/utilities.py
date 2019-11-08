import os

def file_reader(file_name):
    path = os.path.expanduser("~/downloads/" + file_name)
    with open(path, "r") as file:
        s = file.read()
    return s.split("\n")[:-1]


if __name__ == "__main__":
    l = file_reader("rosalind_mer.txt")
    print(len(l))