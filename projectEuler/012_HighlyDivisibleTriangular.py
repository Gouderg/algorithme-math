'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
'''

def isPrime(num):
    i = 2
    while i <= int(num**0.5)+1:
        if num % i == 0 and num != i:
            return False
        i += 1
    return True

def findPrimeNumber():
    i = 2
    primeNumber = []
    while len(primeNumber) <= 1000:
        if isPrime(i):
            primeNumber.append(i)
        i += 1
    return primeNumber

def nbfactorPrime(num, primeNumber):
    nbFactor = dict()
    for elt in primeNumber:
        while num % elt == 0:
            if (elt in nbFactor):    
                nbFactor[elt] += 1
            else:
                nbFactor[elt] = 1
            num = num / elt

    divisor = 1
    for key in nbFactor:
        divisor *= (nbFactor[key] + 1)
    return divisor


triangle = 0
# Génération des 100 premiers nombres premiers
primeNumber = findPrimeNumber()

i = 1
while True:
    triangle += i
    nombre = nbfactorPrime(triangle, primeNumber)
    print(nombre)
    if nombre >= 500:
        print(i, triangle)
        break
    i += 1