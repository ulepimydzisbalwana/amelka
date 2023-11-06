# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:40:18 2023

@author: student
"""
def sprawdz_wliscie(lista, wartosc):
    return wartosc in lista

lista = [2,4,5,7,8,9,]
szukana_wartosc = int(input("Podaj liczbę: "))

wynik = sprawdz_wliscie(lista, szukana_wartosc)

if wynik:
    print(f"Wartość {szukana_wartosc} znajduje się w liście.")
else:
    print(f"Wartość {szukana_wartosc} nie znajduje się w liście.")