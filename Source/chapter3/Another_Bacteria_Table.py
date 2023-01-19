import math

number_of_bacteria = 200
hours = int(input("enter the time of bacteria"))
print("{Hour:>2}, {time:>10}")
for n in range(5, 20, 5):
    time = 200 * math.pow(2, hours)
    n += 1
    print(f"{n:>2}, {time:>15.2f}")
