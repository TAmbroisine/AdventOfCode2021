from itertools import count
import os

DAY = 9

def get_input():
    """Get the input from a txt file"""
    path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/InputDay{}.txt".format(path, DAY)) as Input:
        Input_r = Input.readlines()
    return parse(Input_r)

def parse(input_s):
    """Organize data"""
    grid = []
    for line in input_s:
        temp,trash = line.split("\n")
        grid.append(temp)
    return grid

def find_low_points(grid):
    lr_points = []
    lr_points_x = []
    lr_points_y = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != '9':
                if x == 0:
                    if y == 0:
                        if min(grid[x][y],grid[x+1][y],grid[x][y+1]) == grid[x][y]:
                            lr_points.append(grid[x][y])
                            lr_points_x.append(x)
                            lr_points_y.append(y)
                    elif y == len(grid[x])-1:
                        if min(grid[x][y],grid[x+1][y],grid[x][y-1]) == grid[x][y]:
                            lr_points.append(grid[x][y])
                            lr_points_x.append(x)
                            lr_points_y.append(y)
                    else:
                        if min(grid[x][y],grid[x+1][y],grid[x][y-1],grid[x][y+1]) == grid[x][y]:
                            lr_points.append(grid[x][y])
                            lr_points_x.append(x)
                            lr_points_y.append(y)
                elif x == len(grid)-1:
                    if y == 0:
                        if min(grid[x][y],grid[x-1][y],grid[x][y+1]) == grid[x][y]:
                            lr_points.append(grid[x][y])
                            lr_points_x.append(x)
                            lr_points_y.append(y)
                    elif y == len(grid[x])-1:
                        if min(grid[x][y],grid[x-1][y],grid[x][y-1]) == grid[x][y]:
                            lr_points.append(grid[x][y])
                            lr_points_x.append(x)
                            lr_points_y.append(y)
                    else:
                        if min(grid[x][y],grid[x-1][y],grid[x][y+1],grid[x][y-1]) == grid[x][y]:
                            lr_points.append(grid[x][y])
                            lr_points_x.append(x)
                            lr_points_y.append(y)
                else:
                    if y == 0:
                        if min(grid[x][y],grid[x-1][y],grid[x+1][y],grid[x][y+1]) == grid[x][y]:
                            lr_points.append(grid[x][y])
                            lr_points_x.append(x)
                            lr_points_y.append(y)
                    elif y == len(grid[x])-1:
                        if min(grid[x][y],grid[x-1][y],grid[x+1][y],grid[x][y-1]) == grid[x][y]:
                            lr_points.append(grid[x][y])
                            lr_points_x.append(x)
                            lr_points_y.append(y)
                    else:
                        if min(grid[x][y],grid[x-1][y],grid[x+1][y],grid[x][y-1],grid[x][y+1]) == grid[x][y]:
                            lr_points.append(grid[x][y])
                            lr_points_x.append(x)
                            lr_points_y.append(y)
    return lr_points,lr_points_x,lr_points_y

def call_find_basin(grid,lr_points_x,lr_points_y):
    list_size_basin = []
    for x,y in zip(lr_points_x,lr_points_y):
        basin_locations =[(x,y)]
        basin_locations= find_basin(grid,x,y,basin_locations)
        list_size_basin.append(len(basin_locations))
    list_size_basin.sort()
    return list_size_basin[-3]*list_size_basin[-2]*list_size_basin[-1]

def find_basin(grid,x,y,basin_locations):
    if x-1 > -1 and grid[x-1][y] != '9' and grid[x-1][y] > grid[x][y] and (x-1,y) not in basin_locations:
        basin_locations.append((x-1,y))
        basin_locations= find_basin(grid,x-1,y,basin_locations)
    if x+1 < len(grid) and grid[x+1][y] != '9' and grid[x+1][y] > grid[x][y] and (x+1,y) not in basin_locations:
        basin_locations.append((x+1,y))
        basin_locations= find_basin(grid,x+1,y,basin_locations)
    if y-1 > -1 and grid[x][y-1] != '9' and grid[x][y-1] > grid[x][y] and (x,y-1) not in basin_locations:
        basin_locations.append((x,y-1))
        basin_locations= find_basin(grid,x,y-1,basin_locations)
    if y+1 < len(grid[x]) and grid[x][y+1] != '9' and grid[x][y+1] > grid[x][y] and (x,y+1) not in basin_locations:
        basin_locations.append((x,y+1))
        basin_locations= find_basin(grid,x,y+1,basin_locations)
    return basin_locations

def sum_risk(lr_points):
    total_risk = 0
    for x in lr_points:
        total_risk += int(x)+1
    return total_risk

def part_1():
    grid = get_input()
    lr_points,lr_points_x,lr_points_y = find_low_points(grid)
    return sum_risk(lr_points)

def part_2():
    grid = get_input()
    lr_points,lr_points_x,lr_points_y = find_low_points(grid)
    return call_find_basin(grid,lr_points_x,lr_points_y)
    


print(part_1())
print(part_2())
