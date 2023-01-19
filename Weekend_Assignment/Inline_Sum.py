def sums(a, b, c, d):
    totals = a + b + c + d
    return totals


if __name__ == '__main__':
    s, t, u, v = input("Enter all four digit at once:").split(",")

    print(sums(int(s), int(t), int(u), int(v)))
