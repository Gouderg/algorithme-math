#Calcule le plus petit nombre divisible par les nombres allant de 1 à n

allp = []

def pgcd (a, b):
	if (b == 0): return a
	c = a % b
	return pgcd(b , c)

def ppcm (a, b):
	return int(abs(a * b) / pgcd(a, b))

def fillAllp ():
	for i in range(0,40):
		allp.append(ppcm(i, allp[i - 2]))

fillAllp()

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	print(allp[n - 1])