import os

DAY = 6

def get_input():
    """Get the input from a txt file"""
    path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/InputDay{}.txt".format(path, DAY)) as Input:
        Input_r = Input.read()
        data = parse(Input_r)
    return data


def parse(input_s):
    """Organize data"""
    return [int(n) for n in input_s.split(',')]

def fish_counter(day_by_fish):
    """create a list where each case represents the number with n days due until childbirth"""
    counter_fish = [0]*9
    for fish in day_by_fish:
        counter_fish[fish] += 1
    return counter_fish

def time(counter_fish,day_passed):
    """modelize the time passing for the fish"""
    if day_passed !=0:
        temp = counter_fish[8]
        for i in range(7,-1,-1):
            trash = counter_fish[i]
            counter_fish[i] = temp
            temp = trash
        counter_fish[8] = temp
        counter_fish[6] += temp
    day_passed+=1    
    return day_passed

def sum_fish(counter_fish):
    """Count how many fish there is"""
    total_fish = 0
    for n in counter_fish:
        total_fish += n
    return total_fish

def part_1(day_by_fish):
    day_passed = 0
    counter_fish = fish_counter(day_by_fish)
    for i in range (81):
        # print(str(day_passed))
        day_passed = time(counter_fish,day_passed)
    print("Jour {} : {}".format(day_passed,counter_fish))
    return str(sum_fish(counter_fish))

def part_2(day_by_fish):
    day_passed = 0
    counter_fish = fish_counter(day_by_fish)
    for i in range (257):
        # print(str(day_passed))
        day_passed = time(counter_fish,day_passed)
    print("Jour {} : {}".format(day_passed,counter_fish))
    return str(sum_fish(counter_fish))


data = get_input()
print(part_1(data))
print(part_2(data))