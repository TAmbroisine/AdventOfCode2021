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


def setup_grid_p2(input_s):
    return [[int(n) for n in line.split()] for line in input_s.splitlines()]

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

def find_basin(grid,lr_points_x,lr_points_y):
    temp = 1
    for x,y in zip(lr_points_x,lr_points_y):
        temp_x = x
        temp_y = y
        size_basin = 1
        limit = 0
        debug_x = x
        debug_y = y
        debug_value = grid[x][y]
        max_y,size_basin = find_max_y(grid,temp_x,temp_y,limit,size_basin)
        debug_max_y = max_y
        min_y,size_basin = find_min_y(grid,temp_x,temp_y,limit,size_basin)
        debug_min_y = min_y
        for i in range(min_y,max_y):
            size_basin = find_min_x(grid,temp_x,i,limit,size_basin)
            size_basin = find_max_x(grid,temp_x,i,limit,size_basin)
        print(size_basin)
        temp = temp * size_basin
    return temp


def find_max_x(grid,temp_x,temp_y,limit,size_basin):
    max_x = temp_x
    Debug_max_x = len(grid)-1
    Debug_max_y = len(grid[0])-1
    if temp_x != len(grid)-1:
        Debug_temp_x = temp_x
        Debug_temp_y = temp_y
        while(grid[temp_x+1][temp_y] != '9' and int(grid[temp_x+1][temp_y])>int(grid[temp_x][temp_y])):
            Debug_current_value = grid[temp_x][temp_y]
            Debug_next_value = grid[temp_x+1][temp_y]
            size_basin += 1
            max_x = temp_x
            if temp_x < len(grid)-1:
                temp_x += 1
            else:
                return size_basin
    return size_basin

def find_min_x(grid,temp_x,temp_y,limit,size_basin):
    min_x = temp_x
    if temp_x !=0:
        Debug_temp_x = temp_x
        Debug_temp_y = temp_y
        while(grid[temp_x-1][temp_y] != '9' and int(grid[temp_x-1][temp_y])>int(grid[temp_x][temp_y])):
            Debug_current_value = grid[temp_x][temp_y]
            Debug_next_value = grid[temp_x-1][temp_y]
            size_basin += 1
            if temp_x > 0:
                temp_x -= 1 
            else:
                return size_basin
    return size_basin

def find_min_y(grid,temp_x,temp_y,limit,size_basin):
    min_y = temp_y
    if temp_y !=0:
        Debug_temp_x = temp_x
        Debug_temp_y = temp_y
        while(grid[temp_x][temp_y-1] != '9' and int(grid[temp_x][temp_y-1])>int(grid[temp_x][temp_y])):
            Debug_current_value = grid[temp_x][temp_y]
            Debug_next_value = grid[temp_x][temp_y-1]
            size_basin += 1
            min_y = temp_y
            if temp_y > 0:
                temp_y -= 1 
            else:
                return size_basin
    return min_y,size_basin

def find_max_y(grid,temp_x,temp_y,limit,size_basin):
    max_y = temp_y
    if temp_y != len(grid[temp_x])-1:
        Debug_temp_x = temp_x
        Debug_temp_y = temp_y
        while(temp_y < 9 and grid[temp_x][temp_y+1] != '9' and int(grid[temp_x][temp_y+1])>int(grid[temp_x][temp_y])):
            Debug_current_value = grid[temp_x][temp_y]
            Debug_next_value = grid[temp_x][temp_y+1]
            size_basin += 1
            max_y = temp_y
            if temp_y < len(grid[temp_x])-1:
                temp_y += 1 
            else:
                return size_basin
    return max_y,size_basin



def sum_risk(lr_points):
    total_risk = 0
    print(lr_points)
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
    return find_basin(grid,lr_points_x,lr_points_y)


print(part_1())
print(part_2())
