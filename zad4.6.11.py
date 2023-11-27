# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:36:27 2023

@author: student
"""


def check(a, b, c):
    suma_ab = a + b
    return suma_ab >= c


liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))

wynik = check(liczba1, liczba2, liczba3)

if wynik:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej.")
else:
    print("Suma dwóch pierwszych liczb nie jest większa lub równa trzeciej.")
