if __name__ == '__main__':
    list_1 = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
    list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    double_dict = dict()
    for a in range(10):
        double_dict[list2[a]] = list_1[a]
    print(double_dict)
