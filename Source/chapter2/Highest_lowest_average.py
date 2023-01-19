number1 = int(input('enter a number::'))
number2 = int(input('enter a number::'))
number3 = int(input('enter a number::'))

average = (number1 + number2 + number3) / 3
highest = max(number1, number2, number3)
lowest = min(number1, number2, number3)

print(f"the highest is{highest}\n the lowest is{lowest}\n the average is{average}")
