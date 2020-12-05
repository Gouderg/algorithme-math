'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
prime_occurences = [0,2,3]

def isPrime(num):
    i = 2
    while i <= int(num**0.5)+1:
        if num % i == 0 and num != i:
            return False
        i += 1
    return True


position = 10001

try:
    if prime_occurences[position]:
        print(prime_occurences[position])
except:
    ptr = len(prime_occurences)
    i = ptr - 1
    num = prime_occurences[i]+1
    while ptr <= position:
        if isPrime(num):
            prime_occurences.append(num)
            ptr += 1
        num += 1
    print(prime_occurences[position])