'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
'''

pyramid = []

with open("input/input018.txt", 'r') as file:
    for row in file:
        row = row.replace('<br />\n','')
        pyramid.append(row)

total, idValue = 0, 0

# Parcourir chaque branche et trouvé le plus grand nombre par rapport à l'interval parent

for branch in pyramid:
    branch = [int(elt) for elt in branch.strip().split()]
    if len(branch) == 1:
        total += branch[0]
    elif len(branch) == 2:
        total += max(branch)
        idValue = branch.index(max(branch))
    else:
        total += max(branch[idValue:idValue+2])
        idValue = branch[idValue:idValue+2].index(max(branch[idValue:idValue+2])) + idValue

    print(total,branch[idValue], idValue)
print("Not Finish Working Progress")