#!/usr/bin/env python3
import math
import cmath
import sys

def get_int(msg, minimum, default):
    while True:
        try:
            line =input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >= ", minimum)
            else:
                return i
        except ValueError as e:
            print(e)

def list_find(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index += 1
    else:
        index = -1
    return index

def heron(a,b,c,*,units="meters"):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return"{0} {1}".format(area,units)

def get_string(message, name="string", default=None, minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(name))
                if not(minimum_length <= len(line) <= maximum_length):
                    raise ValueError("{0} must have at least {1} and "
                    "at most {2} characters".format(name, minimum_length, maximum_length))
                return line
        except ValueError as err:
            print("ERROR", err)

def equal_float(a,b):
    return math.abs(a-b) <= sys.float_info.epsilon

def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x

def quadratic():
    print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
    a = get_float("enter a: ", False)
    b = get_float("enter b: ", True)
    c = get_float("enter c: ", True)

    x1 = None
    x2 = None
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant == 0:
        x1 = -(b / (2 * a))
    else:
        if discriminant > 0:
            root = math.sqrt(discriminant)
        else: # discriminant < 0
            root = cmath.sqrt(discriminant)
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)

    if abs(b) < sys.float_info.epsilon:
        b_string = ""
    elif b < 0:
        b_string = "- " + str(abs(b)) + "x "
    else:
        b_string = "+ " + str(b) + "x "
    
    if abs(c) < sys.float_info.epsilon:
        c_string = ""
    elif c < 0:
        c_string = "- " + str(abs(c))
    else:
        c_string = "+ " + str(c)

    equation = ("{0}x\N{SUPERSCRIPT TWO} {1}{2} = 0"
            " \N{RIGHTWARDS ARROW} x = {3}").format(a, b_string, c_string, x1)
    if x2 is not None:
        equation += " or x = {0}".format(x2)
    print(equation)

