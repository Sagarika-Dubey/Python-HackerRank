#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    logo = {}
    for i in s:
        if i not in logo:
            logo[i] = s.count(i)
    sort_logo = sorted(logo.items(), key = lambda x: (- x[1], x[0]))
    for i in range(3):
        print(sort_logo[i][0], sort_logo[i][1])
