'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

    a + b + c = n

    a^2 + b^2 = c^2

    c = n - a - b => (n - a - b)**2 = a**2 + b**2
    => b = (n**-2an)/(2n-2a)
    => c = n - a - b 

'''

n = 1000
maxValue = -1
for a in range(1,n//3):
    b = int((n**2 - 2 * n * a) / (2 * n - 2 * a))
    c = n - a - b
    if a > b: break
    if a**2+b**2 == c**2 and a+b+c == n:
        maxValue = a*b*c

print(maxValue)  