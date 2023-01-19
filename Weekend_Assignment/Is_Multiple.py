def multiple(a, b):
    total = b % a
    if total == 0:
        print("true")
    else:
        print("false")


if __name__ == '__main__':
    m = int(input("enter a number:"))
    n = int(input("enter the second number:"))
    print(multiple(m, n))
