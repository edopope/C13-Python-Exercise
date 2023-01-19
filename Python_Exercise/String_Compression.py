def compress(strings):
    index = 0
    compressed = ""
    length_of_string = len(strings)
    while index != length_of_string:
        count = 1
        while (index < length_of_string - 1) and (strings[index] == strings[index + 1]):
            count = count + 1
            index = index + 1
        if count == 1:
            compressed += str(strings[index])
        else:
            compressed += str(strings[index]) + str(count)
        index = index + 1
    return compressed


if __name__ == '__main__':
    # letters = "aabcccdddddd"
    letters = "abcd"
    print(compress(letters))
