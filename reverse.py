with open("test.txt") as f, open ("reverse.txt", "w") as r:
    lst = []
    for line in f:
        lst.append(line)
    lst.reverse()
    for i in range(len(lst)):
        r.write(lst[i])
