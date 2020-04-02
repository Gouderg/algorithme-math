#Calcule la différence absolue entre la somme des carrées et la somme au carrée

def sumSquare(n):
    sumAll = 0
    sumIntemp = 0

    for i in range(1,n+1):
        sumAll += i*i
        sumIntemp += i
    
    return abs(sumIntemp**2 - sumAll) 

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sumSquare(n))
