#Calcule la somme des multiples de 3 et de 5 jusqu'à 10 en O(1)
t = 2
n = 10

a = ((n-1)//3) 
b = ((n-1)//5) 
c = ((n-1)//15) 
sum = (((3 * a * (a+1))//2) + ((5 * b * (b+1))//2) - ((15 * c * (c+1))//2)) 
print(int(sum))
