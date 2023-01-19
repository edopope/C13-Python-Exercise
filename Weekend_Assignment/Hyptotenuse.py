import math

if __name__ == '__main__':
    side1 = float(input("Enter the length of the opposite side:"))
    side2 = float(input("Enter the length of the adjacent side:"))
    side_opp = math.pow(side1, 2)
    side_adj = math.pow(side2, 2)
    result = side_opp + side_adj
    result2 = math.sqrt(result)
    print("THE HYPOTENUSE IS ", + result2)

