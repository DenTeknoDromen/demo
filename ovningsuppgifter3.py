# 5.1
# tal = input(":")
# try:
#     tal = int(tal)
#     tal = tal*2
#     print(f"Resultat: {tal}")
# except ValueError:
#     print(f"Fel: {tal} kan inte översättas till ett heltal")


# 5.2
# a = input("a: ")
# b = input("b: ")
# c = 0
# try:
#     a = float(a)
#     b = float(b)
#     c = a/b
#     print(f"{a} / {b} = {c}")
# except ZeroDivisionError:
#     print("Ogiltigt nummer")
# except ValueError:
#     print("Ogiltigt nummer")


# 5.3
# kvant = 0
# value = (0)
# indata = input(":")
# while indata != "exit":
#     try:
#         num = int(indata)
#         kvant += 1
#         value += num
#     except ValueError:
#         print("Fel, ogiltigt nummer")
#     indata = input(":")
# print(f"Kardinalitet: {kvant}")
# print(f"Summa: {value}")
# print(f"Medelvärde: {float(value/kvant)}")


# 6.1
# strinput = input("Ange en mening: ").casefold()
# charinput = input("Ange en bokstav:").casefold()
# a = 0

# index = 0
# while index < len(strinput):
#     if strinput[index] == charinput:
#         a += 1
#     index += 1
# print(f"{charinput} förekommer {a} gånger i texten")


# 6.2
# konsonant = "bcdfghjklmnpqrtvwxz"
# indata = input(":")
# newstr = ""

# index = 0
# while index < len(indata):
#     if indata[index].casefold() in konsonant:
#         newstr += f"{indata[index]}o{indata[index].casefold()}"
#     else:
#         newstr += indata[index]
#     index += 1
# print(newstr)


# 6.3
# indata = input(":")
# heap = []
# stack = []

# i = 0
# while i < len(indata):
#     if indata[i] == " ":
#         i += 1
#     else:
#         heap.insert(0, indata[i].casefold())
#         stack.append(indata[i].casefold())
#         i += 1
# if heap == stack:
#     print(f"{indata} är ett palindrom")
# else:
#     print(f"{indata} är inte ett palindrom")

# 6.3 ALT
# indata = input(": ")
# indata = indata.replace(" ", "").casefold()
# palindrom = bool(1)

# i = 0
# while i < int(len(indata)/2):
#     if indata[i] != indata[(i+1)*(-1)]:
#         palindrom = 0
#     i += 1
# if palindrom:
#     print(f"{indata} är ett palindrom")
# else:
#     print(f"{indata} är inte ett palindrom")

# 6.4
# import os

# ui_width = 60
# POST_1 = ""
# POST_2 = ""
# POST_3 = ""
# cont = bool(1)
# while cont:
#     os.system("cls")
# # [ ] 1. Rensa terminalf ¨o nster
# # [ X ] 2. Skriv ut instruktioner
#     print(" .: basicBILLBOARD :. ".center(ui_width))
#     print(ui_width * "*")
#     print(f" P1 : {POST_1}".center(ui_width))
#     print(f" P2 : {POST_2}".center(ui_width))
#     print(f" P3 : {POST_3}".center(ui_width))
#     print(ui_width * "-")
#     print("c | Ändra post ".center(ui_width))
#     print("e | Stäng program ".center(ui_width))
#     print(ui_width * "-")
#     print("Tryck enter för att fortsätta ... ".center(ui_width))
#     indata = input(" ".center(int(ui_width/2)))
#     if indata == "e":
#         cont = False
# [ ] 3. H ¨a mta kommando fr ˚a n anv ¨a ndaren
# [ ] 4. Utf ¨o r operationer f ¨o r inmatat kommando
# [ X ] 5. Pausa exekvering
#
# input("Tryck enter för att forts ¨a tta ... ")
# [ X ] 6. G ˚a till 1
# 8.2
todos = ["Städa", "Handla", "Plugga", "Ge blod"]
print(todos)
todos.append(input("Lägg till ny todo: "))
todos.sort()
print(todos)
todos.pop(int(input("Ta bort todo (index): ")))
print(todos)
todos.remove(input("Ta bort todo (värde): "))
print(todos)
indata = input("Ange todo: ")
if indata in todos:
    print(f"{indata} finns redan i listan")
else:
    print(f"\"{indata}\" finns inte i listan")
    if input("Vill du lägga till den J/N?: ") == "J":
        todos.append(indata)
