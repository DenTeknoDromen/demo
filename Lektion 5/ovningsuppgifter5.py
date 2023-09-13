# import json
# # 9.1
# total = 1000000
# sum = 0
# for y in range(1, int(total/2)):
#     sum += total
# sum += int(total/2)
# print(sum)


# total2 = 500
# sum = 0
# for x in range(1, total2, 2):
#     sum += x
# print(sum)

# 9.2
# registrerade = ["Anna", "Eva", "Erik", "Lars", "Karl"]
# avanmalningar = ["Anna", "Erik", "Karl"]

# for x in range(0, len(avanmalningar)):
#     if avanmalningar[x] in registrerade:
#         registrerade.remove(avanmalningar[x])
# print(registrerade)

# 9.3
# fornamn = ["Maria", "Erik", "Karl"]
# efternamn = ["Svensson", "Karlsson", "Andersson"]
# for x in range(len(fornamn)):
#     for y in range(len(efternamn)):
#         print(f"{fornamn[x]} {efternamn[y]}")
# 9.4
# todo = ["Städa", "Handla", "Plugga", "Ge Blod"]

# for x in range(len(todo)):
#     print(f"- {todo[x]}")

# 10.1
# startsign = ("| - - - - - - - - - - - - - - - - - - - - - - - - "
# "- - - - - - - - - - - - - - - - - - -|"
# "| # - - - - - - - - - - - - - - - - - - - - - - - - - - - # |"
# "| ### | ")

# stopsign = ("| # ### |"
# "| ### - - - - - - - - - - - - - - - - - - - - - - - - - - - ### ### |"
# "| | | | | | # |"
# "| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
# " - - - - - - - - -|"
# "| C | Change sign message"
# "| E | Exit program"
# "| - - - - - - - - - - - - - - - - - - - - - - - -")

# sing = ""
# indata = ""

# with open("sing.txt") as f:
#     sign = (f"{startsign} {f.read()} {stopsign}")
# while indata != "e":
#     print(sign)
#     if indata == "c":
#         with open("sing.txt", "w+") as f:
#             f.write(input("New sign message: "))
#             sign = (f"{startsign} {f.read()} {stopsign}")
#             indata = ""
#     else:
#         indata = input(":")


# 10.2
# number.csv
# numdict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0,
#            "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

# with open("numbers.csv") as n:
#     file = n.read()

# for x in file:
#     if x != "\n":
#         numdict[x] = numdict[x] + 1
# print(numdict)

# 10.3
# with open("database.csv") as d:
#     names = d.readlines()

# indata = ""
# while True:
#     if indata == "id":
#         print(names[int(input("Enter ID: ")-1)])
#     if indata == "scan_f":
#         fname = input("Enter first name: ")
#         for x in range(len(names)):
#             if fname in names[x]:
#                 print(names[x])
#     if indata == "e":
#         break
#     indata = input(": ")

# 11.1

# random_stuff = [1337, 13.37, "HEJHOPP"]

# print(json.dumps(random_stuff))
# print(json.dumps(random_stuff)[0])
# print(random_stuff)
# print(random_stuff[0])

# 11.2

# my_chars = '["abc", "\u00e5\u00e4\u00f6", "123"]'
# mylist = json.loads(my_chars)

# for x in range(len(mylist)):
#     print(mylist[x])

# 11.3
# sum = 0
# nums = []

# with open("text.txt") as f:
#     oldnums = f.read()

# if len(oldnums) > 0:
#     nums = json.loads(oldnums)
# msg = ": "
# while True:
#     for x in range(len(nums)):
#         sum += nums[x]
#         print(f"#{nums[x] }")
#     print(f"Sum: {sum}")
#     indata = input(msg)
#     if indata == "0":
#         break
#     try:
#         indata = int(indata)
#         if indata not in nums:
#             nums.append(indata)
#             msg = "Number added\n: "
#         else:
#             msg = "Input already used, pick another number\n: "
#     except ValueError:
#         msg = "Wrong input, please only use whole integers\n "
#     sum = 0

# with open("text.txt", "w") as f:
#     f.write(json.dumps(nums))

