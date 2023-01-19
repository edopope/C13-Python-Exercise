import string
if __name__ == '__main__':
    word = input("enter a word")
    key = int(input("enter the key to code with"))
    abc = string.ascii_lowercase
    inverse = abc[key:] + abc[:key]
    print(word.translate(str.maketrans(inverse, abc)))
