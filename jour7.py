import os

DAY = 7


def get_input():
    """Get the input from a txt file"""
    path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/InputDay{}.txt".format(path, DAY)) as Input:
        Input_r = Input.read()
        data = parse(Input_r)
    return data


def parse(input_s):
    """Organize data"""
    x_crabs = [int(n) for n in input_s.split(',')]
    return x_crabs


def sum_fuel(crabs, pos):
    """give the fuel consumption for a given position"""
    """for part 1"""
    fuel_consumption = 0
    for n in crabs:
        fuel_consumption += abs(n - pos)
    return fuel_consumption


def sum_fuel_v2(crabs, pos):
    """give the fuel consumption for a given position"""
    """for part 2"""
    fuel_consumption = 0
    for n in crabs:
        pre_sum = 0
        for i in range(abs(n - pos) + 1):
            pre_sum += i
        fuel_consumption += pre_sum
    return fuel_consumption


def part_1(crabs):
    min_fuel = 2**32
    for pos in range(max(crabs)):
        # print(str(pos))
        min_fuel = min(min_fuel, sum_fuel(crabs, pos))
        # print(str(fuel))

    return min_fuel


def part_2(crabs):
    min_fuel = 2**32
    for pos in range(max(crabs)):
        # print(str(pos))
        fuel = sum_fuel_v2(crabs, pos)
        # print(str(fuel))
        if fuel < min_fuel:
            # print("fuel = {} L inférieur à min_fuel = {} L".format(fuel,min_fuel))
            min_fuel = fuel
    return min_fuel


data = get_input()
print(part_1(data))
print(part_2(data))
