import math
#2.1
#citat = " datatyper har inbyggda metoder "
#print ( citat.swapcase() )

#2.2
#a = float(input())
#b = round(a,0)
#print (b)

#2.2
#print("Vad är ditt förnamn?")
#fornamn = input(":")
#print("Vad är ditt efternamn?")
#efternamn = input(":")
#print(fornamn + " " + efternamn)

# 2.3
# age = int(input())
# agediff = 18 - age
# print("Du är myndig om " + str(agediff) "år")

# 2.4
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# print(max(a,b,c,d,e))

#2.6
tvakorv = int(input("Hur många vill ha två korvar?: "))
trekorv = int(input("Hur många vill ha tre korvar?: "))
tvaveg = int(input("Hur många vill ha två veganska korvar?: "))
treveg = int(input("Hur många vill ha tre veganska korvar?: "))

elever = tvakorv + trekorv + tvaveg + treveg
korv = (tvakorv*2) + (trekorv*3)
veg = (tvaveg*2) + (treveg*3)

# paket = math.ceil(korv/8)
# vegpaket = math.ceil(veg/4)


if korv%8 > 0:
    paket = int(korv/8) + 1
else:
    paket = int(korv/8)

if veg%4 > 0:    
    vegpaket = int(veg/4) + 1
else:
    vegpaket = int(veg/4)


kostnad = (paket*20.95) + (vegpaket*34.95) + (elever*13.95)

print("Vanlig korv: " + str(paket))
print("Vegansk korv: " + str(vegpaket))
print("Dryck: " + str(elever))
print(str(kostnad) + " SEK")



