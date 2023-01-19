def handleException(name, serialNumber):
    if name < 3:
        raise TypeError("Name length must be longer than 3")
    if serialNumber < 6:
        raise TypeError("serialNumber length must be longer than 6")


if __name__ == '__main__':
    name_of_boys = "b"
    serialNumber = "2323232"
    handleException(name_of_boys, serialNumber)
