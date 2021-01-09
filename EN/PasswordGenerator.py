import random
ifinput = True
charactersFile = open("characters.txt", "r")
numberTry = 0
characterNumber = 0
password = ""
characterList = [""]
while ifinput:
    try:
        lenght = int(input("Length: "))
        ifinput = False
    except ValueError:
        print("Error: input is not a number")
        ifinput = True
for character in charactersFile.readline():
    characterNumber += 1
    characterList.append(character)
while lenght > numberTry:
    numberTry += 1
    password = password + random.choice(characterList)
print("Generated password:\n")
print(password)
