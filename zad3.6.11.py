# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:32:00 2023

@author: student
"""
def czy_parzysta(liczba):
    return liczba % 2 == 0

liczba = int(input("Podaj liczbę: "))
wynik = czy_parzysta(liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
