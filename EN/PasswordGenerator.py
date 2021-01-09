# Copyright(c) 2020, 2021 'Emil105105' [github.com/Emil105105]
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 
# as published by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
