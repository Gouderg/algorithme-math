'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
palindrome = []

for i in range(101,999):
	for j in range(101,999):
		p = i*j
		if str(p) == str(p)[::-1] and p not in palindrome:
			palindrome.append(p)

palindrome.sort()

n = 999*999
for i in reversed(palindrome):
	if i < n:
		print(i)
		break

