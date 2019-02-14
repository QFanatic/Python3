#!/usr/bin/env python3
import locale
import sys
import unicodedata
locale.setlocale(locale.LC_ALL,"")


def print_unicode_table(word):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode) # Stop at surrogate pairs

    while code < end:
        c = chr(code)
        test = True
        name = unicodedata.name(c, "*** unknown ***")
        if word == []:
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                  code, name.title()))
        else:
            for w in word:
                if w not in name.lower():
                    test = False
                    break
            if test:
                print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                    code, name.title()))                
        code += 1


word = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string][string]...[string]".format(sys.argv[0]))
        word = None
    else:
        for string in sys.argv[1:]:
            word.append(string.lower())
if word is not None:
    print_unicode_table(word)
