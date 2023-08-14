#!/usr/bin/python3
def main():
    a = 89
    b = 10
    a, b = b, a
    print("a={:d} - b={:d}".format(a, b))

if __name__ == "__main__":
    main()
