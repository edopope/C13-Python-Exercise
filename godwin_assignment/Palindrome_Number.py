# if __name__ == '__main__':
#     number = input("ENTER A NUMBER::")
#     index = 0
#     counter = 0
#     while index < len(number):
#         if number[index] == number[len(number) - index - 1]:
#             counter += 1
#             index += 1
#
#     if counter == len(number):
#         print("its a palindrome number")
#     else:
#         print("its not a palindrome number")

name = "jaja"
name2 = str.casefold(name)
rev= reversed(name)
if list(name2) == list(rev):
    print("its a palindrome")
else:
    print("its not a palindrome")

    name_Of_Colors = str(input("enter a string::"))
    if name_Of_Colors == name_Of_Colors[::-1]:
        print("its a palindrome")
    else:
        print("its not a palindrome")
