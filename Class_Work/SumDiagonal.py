def isDiagonal(array):
    add = 0
    index = 0
    for i in range(0, len(array)):
        add = add + array[index][i]
        index += 1
    return add


if __name__ == '__main__':
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(isDiagonal(x))
