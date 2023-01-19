def parameter(lists, value):
    for y in range(len(lists)):
        for x in range(y + 1, len(lists)):
            if lists[y] + lists[x] == value:
                return y, x



if __name__ == '__main__':
    arr = [2, 15, 17, 72, 73, 6, 8, 2, 6, 9, 7]
    print(parameter(arr, 9))
