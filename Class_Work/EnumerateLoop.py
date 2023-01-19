# x = ("ore", "desmond", "dean", "forever")
# for x, y in enumerate(x):
#     print( y)


def missingValue(value):
    for number in range(len(value)):
        if number not in value:
            return number


if __name__ == '__main__':
    # arr = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
    # print(missingValue(arr))

    array = [1, 2, 3, 4, 5, 6, "u", "g"]
    if 2 in array:
        print("name already taken.....enter another name:")
    else:
        print("successfully registered")

