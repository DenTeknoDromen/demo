import random
import klasser
import datetime

lst_rectangles = []


def areasum():
    sum = 0
    for x in lst_rectangles:
        sum += x.getarea()
    return sum


for x in range(1000):
    new_rect = klasser.rectangle(random.randint(1, 100),
                                 random.randint(1, 100))
    lst_rectangles.append(new_rect)

print(f"Summan av areorna är: { areasum()}")

nyperson = klasser.person("Tobias", 27, "Emågatan 90")
print(nyperson)

newcircle = klasser.circle(5)
print(f"Cirkelns omkrets är: {newcircle.getcircum()}")

new_account = klasser.bankaccount("1995", 100)
print(new_account.getkontonummer())
print(new_account.getsaldo())
new_account.deposit(50)
print(new_account.getsaldo())
new_account.withdraw(51)
print(new_account.getsaldo())

dt = datetime.date(2018, 12, 13)
print(dt)
new_employee = klasser.employee("Tobias", 155, dt)
print(f"{new_employee.time()} år")

grades = []
for x in range(10):
    grades.append(random.randint(0, 10))

new_student = klasser.student("Tobias", grades)
print(new_student.get_grades())
