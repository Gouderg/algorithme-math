#Calcule le plus grand produit pour former un palindrome
palindrome = []

for i in range(101,999):
	for j in range(101,999):
		p = i*j
		if str(p) == str(p)[::-1] and p not in palindrome:
			palindrome.append(p)

palindrome.sort()

n = 800000
for i in reversed(palindrome):
	if i < n:
		print(i)
		break;
