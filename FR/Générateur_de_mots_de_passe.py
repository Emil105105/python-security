# Copyright(c) 2020, 2021 'Emil105105' [github.com/Emil105105]
# Ce programme est un logiciel libre ; vous pouvez le redistribuer
# ou le modifier suivant les termes de la GNU General Public License version 3
# telle que publiée par la Free Software Foundation 
# 
# Ce programme est distribué dans l'espoir qu'il sera utile, mais SANS AUCUNE GARANTIE ; 
# sans même la garantie tacite de QUALITÉ MARCHANDE ou d'ADÉQUATION à UN BUT PARTICULIER.
# Consultez la GNU General Public License pour plus de détails.
# Vous devez avoir reçu une copie de la GNU General Public License en même temps que ce programme ;
# si ce n'est pas le cas, consultez <http://www.gnu.org/licenses>.

import random
ifinput = True
charactersFile = open("caractère.txt", "r")
numberTry = 0
characterNumber = 0
password = ""
characterList = [""]
while ifinput:
    try:
        lenght = int(input("Longueur du mot de passe: "))
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
print("Mot de passe généré:\n")
print(password)
