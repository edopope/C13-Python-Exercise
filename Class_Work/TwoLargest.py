def twoLargest(array):
    largest = 0
    secondLargest = 0
    for number in range(len(array)):
        if array[number] > largest:
            secondLargest = largest
            largest = array[number]
    return [largest, secondLargest]


if __name__ == '__main__':
    arrayList = [1, 2, 3, 4, 5, 5]
    print(twoLargest(arrayList))
