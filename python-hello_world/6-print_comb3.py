#!usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print("{:2d}".format(i), "{:2d}".format(j), end=", " if i < 8 or j < 9 else "\n")
