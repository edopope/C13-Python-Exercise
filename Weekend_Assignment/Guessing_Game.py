import random

if __name__ == '__main__':

    my_Number = random.randint(1, 30)
    count = 1
    select = ""
    while select != "no":
        digit = int(input("enter a number -->"))

        if digit == my_Number:
            print("you are correct")
            break
        elif digit < my_Number:
            print("too low")
        elif digit > my_Number:
            print("too high")
        if count == 3:
            print(f'The correct number was {my_Number}')

        select = input("do you want play again yes or no:")

        count += 1
