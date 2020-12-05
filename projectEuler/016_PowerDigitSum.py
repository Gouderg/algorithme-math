'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

somme = 0
for elt in str(2**1000):
    print(elt)
    somme += int(elt)

print(somme)