'''
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
'''
nombre = ''
with open('input/input008.txt','r') as file:
    for row in file:
        row = row.replace('<br />','')
        row = row.replace('\n','')
        nombre += row


n = [len(nombre), 13]

produitMax = -1
for i in range(0,n[0]-n[1]+1):
    temp = nombre[i:i+n[1]]
    temp = [int(elt) for elt in temp]

    produitTemp = 1
    if 0 in temp:
        produitTemp = 0
    else:
        for elt in temp:
            produitTemp *= elt
    
    if produitTemp > produitMax:
        produitMax = produitTemp

print(produitMax)