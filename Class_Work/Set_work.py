if __name__ == '__main__':
    member_set = set()
    for x in range(5):
        try:

            set_number = int(input("Enter a number between 2 and 90 5 times:"))

            if 2 <= set_number <= 90:
                member_set.add(set_number)
                print(member_set)
            else:
                print("invalid number try again")

        except ValueError:
            print("Oga enter a number")

   