def capitalizeVowel(Strings):
    vowels = ["a", "e", "i", "o", "u"]
    empty = []
    for char in Strings:
        if char in vowels:
            empty.append(char.upper())
        else:
            empty.append(char.lower())

    for newWord in empty:
        print(newWord, end=" ")


if __name__ == '__main__':
    my = "forever"
    (capitalizeVowel(my))
