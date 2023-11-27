# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:12:23 2023

@author: student
"""


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}\n" \
               f"Open hours: {self.open_hours}\n" \
               f"Phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\n" \
               f"Hire date: {self.hire_date}\n" \
               f"Birth date: {self.birth_date}\n" \
               f"Address: {self.city}, {self.street}, {self.zip_code}\n" \
               f"Phone: {self.phone}"


class Book:
    def __init__(self, library, publication_date,
                 author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\n" \
               f"Publication date: {self.publication_date}\n" \
               f"Number of pages: {self.number_of_pages}\n" \
               f"Library: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Employee: {self.employee}\n" \
                f"Student: {self.student}\n" \
                f"Books:\n{', '.join(str(book) for book in self.books)}\n" \
                f"Order Date: {self.order_date}"


library1 = Library("Bytom", "Dworcowa", "12345",
                   "9:00  - 17:00", "123-456-789")
library2 = Library("Zabrze", "3 Maja", "54321",
                   "10:00 - 16:00", "987-654-321")

employee1 = Employee("Jan", "Kowalski", "2022-01-01", "1990-01-01",
                     "Katowice", "Francuska", "12345", "111-222-333")
employee2 = Employee("Marek", "Nowak", "2022-01-02", "1995-02-15",
                     "Warszawa", "Wrocławska", "54321", "444-555-666")
employee3 = Employee("Justyna", "Kowalska", "2022-01-03", "1985-07-10",
                     "Gdańsk", "Sądowa", "12345", "777-888-999")

book1 = Book(library1, "1940-01-01", "Adam", "Mickiewicz", 270)
book2 = Book(library1, "1845-02-01", "Juliusz", "Slowacki", 890)
book3 = Book(library2, "2000-03-01", "Wislawa", "Szymborska", 360)
book4 = Book(library2, "20205-04-01", "Jaroslaw", "SBorszewicz", 300)
book5 = Book(library1, "1994-05-01", "Julian", "Tuwim", 18)

order1 = Order(employee1, "Adrian", [book1, book2, book3], "2022-02-01")
order2 = Order(employee2, "Janusz", [book4, book5], "2022-02-02")

print(order1)
print("\n")
print(order2)
