# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:13:22 2023

@author: student
"""


def przywitanie(name, surname):
    wynik = f"Cześć {name} {surname}!"
    return wynik


# Przykład użycia funkcji
imie = "Jan"
nazwisko = "Kowalski"
powitanie = przywitanie(imie, nazwisko)
print(powitanie)
