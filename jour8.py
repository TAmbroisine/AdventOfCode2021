import os
from ossaudiodev import SNDCTL_DSP_BIND_CHANNEL
import re
from string import digits

DAY = 8


def get_input():
    """Get the input from a txt file"""
    path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/InputDay{}.txt".format(path, DAY)) as Input:
        Input_r = Input.read()
        digits_input,digits_output = parse(Input_r)
    return digits_input,digits_output

def parse(input_s):
    """Organize data"""
    data = [ line.split('\n') for line in input_s.split(' | ')]
    return parse_in_out(data)

def parse_in_out(data):
    digits_in = []
    digits_out = []
    for i,digits in enumerate(data):
        for j,puts in enumerate(digits):
            if i == 0:
                digits_in.append(puts)
            elif i == len(data)-1:
                digits_out.append(puts)
            elif j  == 1:
                digits_in.append(puts)
            else:
                digits_out.append(puts)
    digits_input = [line.split(' ') for line in digits_in]
    digits_output = [line.split(' ') for line in digits_out]
    return digits_input,digits_output

def count_unique_output(digits_output):
    digits_number = ["2","3","4","7"]
    unique_digits = []
    sum = 0
    for digits_list in digits_output:
        for digits in digits_list:
            if str(len(digits)) in digits_number:
                # print ("Il y a {} digits dans {} . Le nombre de digits est unique".format(len(digits),digits))
                sum += 1
    return sum

def create_digits(digits_input,digits_output):
    code_one,code_four,code_seven,code_eight = [],[],[],[]
    code_one,code_four,code_seven,code_eight = create_code(digits_input,code_one,code_four,code_seven,code_eight)
    sum_digicode = create_digicode(digits_output,code_one,code_four)
    return sum_digicode

def create_code(digits,code_one,code_four,code_seven,code_eight):
    for digit in digits:
        if len(digit) == 2:
            for letter in digit:
                code_one.append(letter)
        if len(digit) == 3:
            for letter in digit:
                code_seven.append(letter)
        if len(digit) == 4:
            for letter in digit:
                code_four.append(letter)
        if len(digit) == 7:
            for letter in digit:
                code_eight.append(letter)
    return code_one,code_four,code_seven,code_eight

def create_digicode(digits_output,code_one,code_four):
    digicode = 0
    code_temp=[]
    for n in code_four:
        if n not in code_one:
            code_temp.append(n)
    for i,digit in enumerate(digits_output):
        temp = [j for j in digit]
        if len(temp) == 2:
            digicode += 1*(10**(3-i))
        elif len(temp) == 3:
            digicode += 7*(10**(3-i))
        elif len(temp) == 4:
            digicode += 4*(10**(3-i))
        elif len(temp) == 7:
            digicode += 8*(10**(3-i))
        elif len(temp) == 5:
            if set(code_one).issubset(temp):
                digicode += 3*(10**(3-i))
            elif set(code_temp).issubset(temp):
                digicode += 5*(10**(3-i))
            else:
                digicode += 2*(10**(3-i))
        elif len(temp) == 6:
            if set(code_four).issubset(temp):
                digicode += 9*(10**(3-i))
            elif set(code_temp).issubset(temp):
                digicode += 6*(10**(3-i))
            else:
                digicode += 0*(10**(3-i))
    return digicode

def part_1(digits_output):
    sum = count_unique_output(digits_output)
    return str(sum)

def part_2(digits_input,digits_output):
    sum_digicode = 0
    for i,j in zip(digits_input,digits_output):
        sum_digicode += create_digits(i,j)
    return str(sum_digicode)


sum_digicode = 0
digits_input,digits_output = get_input()

print(part_1(digits_output))
print(part_2(digits_input,digits_output))



