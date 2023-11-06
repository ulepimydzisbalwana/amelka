# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:43:06 2023

@author: student
"""
def dzialania(lista, lista2):
    polaczona_lista = lista + lista2
    unikalne_elementy = list(set(polaczona_lista))
    potegowanie = [x ** 3 for x in unikalne_elementy]

    return potegowanie

lista = [1, 2, 3]
lista2 = [4, 5, 6]

wynik = dzialania(lista, lista2)
print(wynik)