import math
import datetime

class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def getarea(self):
        return self.height * self.width


class person:
    def __init__(self, name, age, adress) -> None:
        self.name = name
        self.age = age
        self.adress = adress

    def __str__(self):
        return f"Det här är {self.name} ({self.age}), han bor på {self.adress}"


class circle:
    def __init__(self, r):
        self.r = r

    def getcircum(self):
        return (2 * math.pi * self.r)


class bankaccount:
    def __init__(self, kontonummer, saldo):
        self.kontonummer = kontonummer
        self.saldo = saldo

    def getkontonummer(self):
        return self.kontonummer

    def getsaldo(self):
        return f"{self.saldo} kr"

    def deposit(self, amount):
        self.saldo += amount

    def withdraw(self, amount):
        self.saldo -= amount


class employee:
    def __init__(self, name, salary, startdate):
        self.name = name
        self.salary = salary
        self.startdate = startdate

    def time(self):
        self.today = datetime.date.today()
        time_diff = self.today - self.startdate
        return math.ceil(time_diff.days / 365)


class student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        return self.name

    def get_grades(self):
        sum = 0
        for x in self.grades:
            sum += x
        return sum / len(self.grades)
