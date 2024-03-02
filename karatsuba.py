def karatsuba(x, y):
    print(x,y)
    if x < 10 and y < 10:
        return x*y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m

    xh = x // p
    xl = x % p

    yh = y // p
    yl = y % p 

    first = karatsuba(xh, yh)
    last = karatsuba(xl, yl)
    mid = karatsuba(xh+xl, yh+yl) - first - last

    return first*(10**(2*m)) + mid*(10**m) + last


# arr = [(5,6), (100,343), (1234,5678), (111221243, 938)]
# for a,b in arr:
#     print(karatsuba(a,b) == a*b)

# print(100*343)
# print(karatsuba(100,343))

print(karatsuba(1234, 5678))