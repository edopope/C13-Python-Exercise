if __name__ == '__main__':
    select = input("select the temperature u want to convert to press(k) for kelvin and (c) for celsius:")
    if select == "k":
        kelvin = int(input("Enter Temp::"))
        solution = kelvin + 273.15
        print(f'your temperature in kelvin is {solution}')
    if select == "c":
        celsius = int(input("Enter TEMP:"))
        solution1 = celsius - 273.15
        print(f'your temperature in celsius is{solution1}')

 