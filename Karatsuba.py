def N(x):
    x //= 10
    n = 1
    while x > 0:
        x //= 10
        n += 1
    return n
def karatsuba(x , y):
    l = 0
    if N(x) == 1: 
        return x * y
    if N(x)%2 !=0:
        x *=10
        l+=1
    if N(y)%2 !=0:
        y *=10 
        l+=1
    while N(y) < N(x) and x!=0 and y!=0:
        y *= 10 
        l+=1
    while N(x) < N(y) and x!=0 and y!=0:
        x *=10 
        l+=1

    n = N(x)
    
   
    a , b=  x // (10**(n//2)), x % (10**(n//2))
    c , d=  y // (10**(n//2)), y % (10**(n//2))
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    
    pq = karatsuba(a+b,c+d)
    adbc = pq - ac -bd
    
    return (ac * (10**n) + adbc * (10 ** (n//2)) + bd )// 10 **l



