indata = ""
with open("text.txt", "r") as f:
    indata = f.read()
indata = indata.replace("â€™", "\'")
indata = indata.replace(" ", "")

with open("text.txt", "w") as f:
    f.write(indata)
