try:
    factor = int(input("Enter a number to check::"))
    for prime in range(1, factor):
        if factor % prime == 0:
            print(prime)
except BaseException:
    print("enter number Abeg ")

