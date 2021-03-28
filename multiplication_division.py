# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 19:12:10 2021
"""

import random
import time

print('=======================================')
print("\t\tMultiplication Tables")
print('=======================================\n')

n=10
for row in range(1, n + 1):
    print(*(f"{row*col:3}" for col in range(1, n + 1)))