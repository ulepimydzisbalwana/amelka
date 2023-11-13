# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:17:23 2023

@author: student
"""

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area} m2, {self.rooms} rooms\n" \
               f"Price: {self.price} zl\n" \
               f"Address: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House - {super().__str__()}\n" \
               f"Plot: {self.plot} m2"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat - {super().__str__()}\n" \
               f"Floor: {self.floor}"


# Stworzenie obiektu klasy House
house1 = House(area=150, rooms=4, price=300000, address="Katowicka 123", plot=500)

# Stworzenie obiektu klasy Flat
flat1 = Flat(area=30, rooms=2, price=150000, address="Bytomska 456", floor=3)

# Wyświetlenie obiektów
print(house1)
print("\n")
print(flat1)


