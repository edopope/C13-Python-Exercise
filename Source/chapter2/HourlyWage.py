import math

if __name__ == '__main__':
    rate = float(input("enter rate:"))
    principal = int(input("enter principal:"))
    number_of_years = int(input("enter the number of years:"))
    new_amount = principal * (math.pow(1 + rate, number_of_years))
    for i in range(1, number_of_years):
        print(new_amount)

