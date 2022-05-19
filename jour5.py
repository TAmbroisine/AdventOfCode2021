from itertools import count
import os
import re
import csv

DAY = 5


def get_input():
    """Get the input from a txt file"""
    path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/InputDay{}.txt".format(path, DAY)) as Input:
        Input_r = Input.read()
        data = parse(Input_r)
    return data


def parse(input_s):
    """Organize data"""
    numbers = re.split('-> |\n', input_s)
    data = [[0, 0] for line in numbers]
    for x, line in enumerate(numbers):
        for y, l in enumerate(line.split(',')):
            data[x][y] = l
    return data


def get_field(data):
    """get the dimensions of the field and create a python object that modelize it"""
    x_field, y_field = 0, 0
    for x in range(len(data)):
        if int(data[x][0]) > x_field:
            x_field = int(data[x][0])
        if int(data[x][1]) > y_field:
            y_field = int(data[x][1])
    x_field += 1
    y_field += 1
    field = [[0] * y_field for x in range(x_field)]
    return field


def locate_vents(data, field, part):
    """Modelize the vents on the field"""
    for i in range(0, len(data), 2):
        x1, x2, y1, y2 = set_xn_yn(data, i)
        diff_x = x2 - x1
        diff_y = y2 - y1
        if x1 == x2:
            for y in range(abs(diff_y) + 1):
                if y2 > y1:
                    field[x1][y1 + y] += 1
                else:
                    field[x1][y2 + y] += 1
        elif y1 == y2:
            for x in range(abs(diff_x) + 1):
                if x2 > x1:
                    field[x1 + x][y1] += 1
                else:
                    field[x2 + x][y1] += 1
        elif part == 2:
            """do the diagonals"""
            if x1 == y1 and x2 == y2:
                for x, y in zip(range(abs(diff_x) + 1),
                                range(abs(diff_y) + 1)):
                    if x2 < x1:
                        field[x2 + x][y2 + y] += 1
                    else:
                        field[x1 + x][y1 + y] += 1
            elif x1 == y2 and x2 == y1:
                for i in range(abs(x1 - y1) + 1):
                    if x1 > y1:
                        field[x1 - i][y1 + i] += 1
                    else:
                        field[x1 + i][y1 - i] += 1
            elif abs(diff_x) == abs(diff_y):
                for i in range(abs(diff_x) + 1):
                    if x1 > x2 and y1 > y2:
                        field[x1 - i][y1 - i] += 1
                    elif x1 > x2 and y2 > y1:
                        field[x1 - i][y1 + i] += 1
                    elif x1 < x2 and y1 > y2:
                        field[x1 + i][y1 - i] += 1
                    else:
                        field[x1 + i][y1 + i] += 1


def set_xn_yn(data, i):
    x1 = int(data[i][0])
    x2 = int(data[i + 1][0])
    y1 = int(data[i][1])
    y2 = int(data[i + 1][1])
    return x1, x2, y1, y2


def debug_locate_vent(field):
    with open("fieldDay5.csv", 'w') as result:
        res_writer = csv.writer(result)
        for line in list(zip(*field)):
            res_writer.writerow(line)


def sum_overlaping_points(field):
    """count how many time there is points overlap each other"""
    count = 0
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[x][y] >= 2:
                count += 1
    return count


def part_1(data):
    """resolve part 1 of day 5"""
    field = get_field(data)
    locate_vents(data, field, 1)
    debug_locate_vent(field)
    return sum_overlaping_points(field)


def part_2(data):
    """resolve part 1 of day 5"""
    field = get_field(data)
    locate_vents(data, field, 2)
    debug_locate_vent(field)
    return sum_overlaping_points(field)


data = get_input()
print(part_1(data))
print(part_2(data))
