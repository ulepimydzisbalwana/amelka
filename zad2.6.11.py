# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:24:10 2023

@author: student
"""


def type_hinting(liczba: int, liczba1: int) -> bool:
    wynik = liczba * liczba1
    return wynik


liczba1 = 10
liczba2 = 4
wynik_mnozenia = type_hinting(liczba1, liczba2)
print(wynik_mnozenia)
