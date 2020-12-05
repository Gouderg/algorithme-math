'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
'''
def facto(n):
    if n <= 1: return 1
    return n*facto(n-1)

def coefBinomiaux(n,k):
    return facto(n)//(facto(n-k)*facto(k))

n, k = 20, 20
print(coefBinomiaux(n+k,n))
