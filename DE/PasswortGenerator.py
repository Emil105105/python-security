# Copyright(c) 2020, 2021 'Emil105105' [github.com/Emil105105]
# Dieses Programm ist Freie Software: Sie können es unter den Bedingungen
# der GNU General Public License Version 3 von der Free Software Foundation,
# weiter verteilen und/oder modifizieren.
# 
# Dieses Programm wird in der Hoffnung bereitgestellt, dass es nützlich sein wird, jedoch
# OHNE JEDE GEWÄHR,; sogar ohne die implizite
# Gewähr der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
# Siehe die GNU General Public License für weitere Einzelheiten.
# 
# Sie sollten eine Kopie der GNU General Public License zusammen mit diesem
# Programm erhalten haben. Wenn nicht, siehe <https://www.gnu.org/licenses/>.

import random
ifinput = True
charactersFile = open("Zeichen.txt", "r")
numberTry = 0
characterNumber = 0
password = ""
characterList = [""]
while ifinput:
    try:
        lenght = int(input("Länge: "))
        ifinput = False
    except ValueError:
        print("Ungülige Zahl")
        ifinput = True
for character in charactersFile.readline():
    characterNumber += 1
    characterList.append(character)
while lenght > numberTry:
    numberTry += 1
    password = password + characterList[random.randint(1, characterNumber)]
print("Ihr generiertes Passwort:\n")
print(password)
