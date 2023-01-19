number = int(input("enter a number to check if its even or odd:"))
# if number % 2 == 0:
#     print("its an even number")
# else:
#     print("its an odd number")
remain = number // 4
if remain == 0:
    print("it can be shared equally")
else:
    print("it cant be shared equally except each person takes", + remain)
