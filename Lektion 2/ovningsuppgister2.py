import random
#3.1
# a = input("Ange ett tal:")
# b = input("Ange ett till tal:")
# c = input("Ange ännu ett tal:")
# maxnum = a
# if b > maxnum:
#     maxnum = b
# if c > maxnum:
#     maxnum = c
# print("Det största inmatade talet är: " + maxnum)

# 3.2
# namn = input("Ange ditt namn: ")
# age = int(input("Ange din ålder: "))

# if age == 1:
#     sleep = 14
# elif age == 2:
#     sleep = 13
# elif age == 3:
#     sleep = 12
# elif age == 4:
#     sleep = 11.5
# elif age == 5 or age== 6:
#     sleep = 11
# elif age == 7:
#     sleep = 10.5
# elif age == 8 or age == 9 or age == 10:
#     sleep = 10
# elif age == 11:
#     sleep = 9.5
# elif age == 12 or age == 13 or age == 14 or age == 15:
#     sleep = 9
# elif age == 16:
#     sleep = 8.5
# else:
#     sleep = 8

# print("Halllå " + namn + "! Enligt Vårdguidens rekommendationer " +
#       "behöver individer i din ålder (" + str(age) + 
#       " år) sova minst " + str(sleep) + " timmar per natt")
#3.2 ALT
# agesleep = {"1":"14",
#             "2":"13",
#             "3":"12",
#             "4":"11,5",
#             "5":"11",
#             "6":"11",
#             "7":"10,5",
#             "8":"10",
#             "9":"10",
#             "10":"10",
#             "11":"9,5",
#             "12":"9",
#             "13":"9",
#             "14":"9",
#             "15":"9",
#             "16":"8,5"
#             }
# namn = input("Ange ditt namn: ")
# age = (input("Ange din ålder: "))
# sleep = 8
# if int(age) < 17:
#     sleep = agesleep[age]

# print("Halllå " + namn + "! Enligt Vårdguidens rekommendationer " +
#        "behöver individer i din ålder (" + str(age) + 
#        " år) sova minst " + str(sleep) + " timmar per natt")

#3.3
# dice = random.randint(1,6)
# if dice == 1:
#     print ("Du slog en 1:a.")
# if dice == 2:
#     print ("Du slog en 2:a!")
# if dice == 3:
#     print ("Du slog en 3:a!")
# if dice == 4:
#     print ("Du slog en 4:a!")
# if dice == 5:
#     print ("Du slog en 5:a!")
# if dice == 6:
#     print ("Du slog en 6:a!")

#3.4
# land = input("Vilket land kommer du ifrån? ").casefold()
# if land == "danmark":
#     print("Du är från Norden")
# elif land == "finland":
#     print("Du är från Norden")
# elif land == "island":
#     print("Du är från Norden")
# elif land == "norge":
#     print("Du är från Norden")
# elif land == "sverige":
#     print("Du är från Norden")
# elif land == "england":
#     print("Du är från Storbrittanien")
# elif land == "nordirland":
#     print("Du är från Storbrittanien")
# elif land == "skottland":
#     print("Du är från Storbrittanien")
# elif land == "wales":
#     print("Du är från Storbrittanien")
# else:
#     print("Du är varken från Norden eller Storbrittanien")
#3.4 ALT
# norden = ["sverige", "danmark", "norge","finland","island"]
# gb = ["england", "wales","nordirland","skottland"]
# land = input("Vilket land kommer du ifrån? ").casefold()
# if land in norden:
#      print("Du är från Norden")
# elif land in gb:
#      print("Du är från Storbrittanien")
# else:
#      print("Du är varken från Norden eller Storbrittanien")
#
#3.5


# 4.1
# minnum = 0
# maxnum = 0
# numnum = 0
# sum = 0

# inputnum = 0
# while inputnum >= 0:
#     if inputnum < minnum:
#         minnum = inputnum
#     if inputnum > maxnum:
#         maxnum = inputnum
#     sum += inputnum
#     numnum += 1
#     inputnum = int(input())

# print("Minsta tal = "+ str(minnum))
# print("Största tal = "+ str(maxnum))
# print("Summa = "+ str(sum))
# print("Medelvärde = "+ str(sum/numnum))

# 4.2
# multi = int(input("Ange multiplikationstabell:"))
# i = 1
# yesno = "y"
# while yesno == "y":
#     print(i * multi)
#     if i%3 == 0:
#           yesno = input("Fortsätt? Y/N)")
#     i += 1


##4.3
# rnd = random.randint(0,99)
# numinput= -1
# numtry = 0
# while numinput != rnd:
#     numinput = int(input(":"))    
#     print("Your guess: " +str(numinput))
#     if numinput>rnd:
#         print("Lower!")
#     elif numinput<rnd:
#         print("Higher!")

# print("The number was " +str(numinput))
