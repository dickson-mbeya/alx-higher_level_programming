for i in range(10):
    for j in range(10):
        if (i-j) < 0:
            print("{}{}".format(i, j), end=", " if i+j < 17 else "\n")
