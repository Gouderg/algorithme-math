'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def isPrime(num):
    i = 2
    while i <= int(num**0.5)+1:
        if num % i == 0 and num != i:
            return False
        i += 1
    return True

n = 2000000
sommePrime = 2

for i in range(3,n):
    if i%2==0:
        pass
    elif isPrime(i):
        sommePrime += i

print(sommePrime)
