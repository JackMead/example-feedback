with open('Calcs.txt', 'r') as calcs_file:
    contents = calcs_file.read()

lines=contents.splitlines()

count=0
for x in lines:
    line=lines[count].split(",")
    line2=line[0].split(" ")
    Operation = (line2[1])
    Number1 = int((line2[2]))
    Number2 = int((line2[3]))
    count +=1

    if Operation == "+":
        print (Number1 + Number2)
    elif Operation == "-":
        print (Number1 - Number2)
    elif Operation == "x":
        print (Number1 * Number2)
    elif Operation == "/":
        print (Number1 / Number2)
