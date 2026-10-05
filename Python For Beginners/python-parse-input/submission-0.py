def read_integers() -> list[int]:
    line = input()
    lst = line.split(",")
    return [int(elem) for elem in lst]


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
