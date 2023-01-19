def isUnique(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return False
    return True


if __name__ == '__main__':
    number1 = ["john","felix","amarachi","john"]
    print(isUnique(number1))
