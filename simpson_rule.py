#!/usr/bin/env python3
import locale
import sys
import math
from decimal import *
locale.setlocale(locale.LC_ALL,"")

def simpson_rule(func, a, b, p=10):
    """Returns the area for a given function(func) between bounds of a to b, using Simpson's method, p determines the number of sections used where sections = 2^p. To double sections just increase p by 1
    """
    n = 2**p
    h = (b-a)/n
    values = []
    for i in range(n):
        values.append(func(a+i*h))
    values.append(func(b))
    evens = sum(values[2:n:2])
    odds = sum(values[1:n:2])
    total = values[0] + values[n] + 2*(evens) + 4*(odds)
    total *= h
    total /= 3
    return total

def simpson_rule_dec(func, a, b, p=10, prec = 28):
    """Returns the area for a given function(func) between bounds of a to b, using Simpson's method, p determines the number of sections used where sections = 2^p. To double sections just increase p by 1.  Uses Pythons Decimal type, precision of Decimal is set by prec.
    """
    getcontext().prec = prec
    n = Decimal(2**p)
    b = Decimal(b)
    a = Decimal(a)
    h = Decimal((b-a)/n)
    values = []
    for i in range(n):
        values.append(func(a+i*h))
    values.append(func(b))
    evens = sum(values[2:n:2])
    odds = sum(values[1:n:2])
    total = Decimal(values[0] + values[n] + 2*(evens) + 4*(odds))
    total *= h
    total /= 3
    return total
