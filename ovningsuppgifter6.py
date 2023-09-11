import json

# notes = {"Meddelande från skolan": "Friluftsdag på tisdag",
#          "Kom ihåg!": "Ta bilen till verkstad",
#          "Inför tentamen": "Gör alla instuderingsuppgifter"}

# 12.1
# while True:
#     indata = input(": ")
#     if indata == "e":
#         break
#     try:
#         print(notes[indata])
#     except KeyError:
#         print("Ange en korrekt nyckel:")
#     except ValueError:
#         print("Ange en korrekt nyckel")

# 12.2
# for keys in notes:
#     print(keys)

# 12.3
# for keys in notes:
#     print(keys)
#     print(notes[keys])
#     print("------------------")

# 12.4
# while True:
#     newkey = input("Ange ny nyckel: ")
#     newvalue = input("Ange ett nytt värde: ")
#     notes[newkey] = newvalue
#     for keys in notes:
#         print(keys)
#         print(notes[keys])
#         print("--------------------------")

# 12.5
# while True:
#     removekey = input("Ta bort artikel: ")
#     try:
#         notes.pop(removekey)
#     except KeyError:
#         print("Ange en korrekt nyckel: ")
#     for keys in notes:
#         print(keys)
#         print(notes[keys])
#         print("--------------------------")

# 13.6
with open("dict.txt") as d:
    notes = json.loads(d.read())


def view():
    while True:
        print("Enter >menu< to return to menu")
        indata = input("Enter note to view: ")
        if indata == "menu":
            break
        try:
            print(f"    - {notes[indata]}\n")
        except KeyError:
            print("PLease enter a valid note:")


def add():
    while True:
        print("Enter >menu< to return to menu")
        newnote = input("Enter name of new note: ")
        if newnote == "menu":
            break
        newvalue = input("Enter contents of note: ")
        if newvalue == "menu":
            break
        notes[newnote] = newvalue


def remove():
    while True:
        print("Enter >menu< to return to menu")        
        indata = input("Enter name of note to remove: ")
        if indata == "menu":
            break
        try:
            del notes[indata]
        except KeyError:
            print("Please enter a valid note")


msg = "Menu"
while True:
    print("Notes")
    print("--------------------------")
    for keys in notes:
        print(f"* {keys}")
        print("--------------------------")
    print(">view     : View notes")
    print(">add      : Add notes")
    print(">rm       : Remove notes")
    print(">exit     : Exit program")
    print("--------------------------")
    print(msg)
    indata = input("> ").casefold()
    if indata == "view":
        view()
    elif indata == "add":
        add()
    elif indata == "rm":
        remove()
    elif indata == "exit":
        break
    else:
        msg = "Please enter a valid command"
    print("--------------------------")

with open("dict.txt", "w") as d:
    d.write(json.dumps((notes)))
