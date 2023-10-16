# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:53:40 2023

@author: student
"""

import random 
lista = [random.random() for x in range(5)]
print(lista)
# z listą składaną 
nowa_lista = [liczba * 2 for liczba in lista]
print(nowa_lista)

#z pętlą for
nowa_lista = []
for liczba in lista:
    nowa_lista.append(liczba * 2)
print(nowa_lista)