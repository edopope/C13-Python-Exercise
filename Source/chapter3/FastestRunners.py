import numpy

first_fastest = 0
second_fastest = 0
counter = 0
runners = int(input("enter the list of runners:"))
while runners != 0:
    runners = int(input("enter the list of runners:"))
    my_runner = numpy.array([runners])
    for runner in my_runner:
        if runner > first_fastest:
            second_fastest = first_fastest
            first_fastest = runner


print(f"the first runner score is{first_fastest}\n,The second runner score is {second_fastest}")
counter += 1

