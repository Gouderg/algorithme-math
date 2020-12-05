'''Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.'''
data = []
with open('input/input013.txt','r') as file:
    for row in file:
        row = row.replace('<br />','')
        row = row.split()
        data.append(row)

somme = 0
for row in data:
    for elt in row:
        somme += int(elt)

carla = str(somme)
print(carla[:10])