#!/usr/bin/env python3

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
