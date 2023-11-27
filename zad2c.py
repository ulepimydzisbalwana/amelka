# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:11:54 2023

@author: student
"""

import random
lista = [random.randint(0, 100) for x in range(10)]
print(lista)
parzyste = []
for el in lista:
    if el % 2 == 0:
        parzyste.append(el)
print(parzyste)
