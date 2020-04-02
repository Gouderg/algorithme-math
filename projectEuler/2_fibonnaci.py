#Calcule la somme des nombres paires de la suite de fibonnaci
from math import sqrt

#Renvoie n terme de la suite de fibonnaci
def nfibonnaci(n):
	result = (1/sqrt(5))*((((1+sqrt(5))/2)**n) - (((1-sqrt(5))/2)**n))
	return int(result)

n = 10
temp = 0
i = 0
result = 0

while temp < n:
	temp = nfibonnaci(i)
	if ((temp % 2) == 0) and (temp < n):
		result += temp
	i += 1

print("Somme =",sum)