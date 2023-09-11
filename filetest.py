word = input(": ")
otherword = input(": ")
with open("romeo.txt") as f:
    text = f.read()

text = text.replace(word, otherword)
text = text.replace(word.casefold(), otherword.casefold())
text = text.replace(word.capitalize(), otherword.capitalize())
text = text.replace(word.upper(), otherword.upper())

with open("romeo.txt", "w") as f:
    f.write(text)
