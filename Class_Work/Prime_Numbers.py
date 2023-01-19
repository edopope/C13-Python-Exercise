from math import sqrt

if __name__ == '__main__':
    number = int(input("enter a number to check if its prime:"))
    check = 0
    if number > 1:
        for z in range(2, int(sqrt(number)) + 1):
            if number % z == 0:
                check = 1
        if check == 0:
            print("its  a prime number")

        else:
            print("its not a prime number")
    else:
        print("its not a prime number")
