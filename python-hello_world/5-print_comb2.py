#!usr/bin/python3
def print_numbers():
    for i in range(100):
        print("{:02}".format(i), end=", ")
        if i == 99:
            print("\n")

if __name__ == "__main__":
    print_numbers()
