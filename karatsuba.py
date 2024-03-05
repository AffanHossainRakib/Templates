def karatsuba(x, y):
    if len(str(x)) == 1 and len(str(y)) == 1:
        return x*y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m

    # xh, xl = divmod(x, p)
    xh = x // p
    xl = x % p

    # yh, yl = divmod(y, p)
    yh = y // p
    yl = y % p 

    first = karatsuba(xh, yh)
    last = karatsuba(xl, yl)
    mid = karatsuba(xh+xl, yh+yl) - first - last

    return first*(10**(2*m)) + mid*(10**m) + last


arr = [(5,6), (100,343), (1234,5678), (111221243, 938)]
for a,b in arr:
    print(karatsuba(a,b) == a*b)