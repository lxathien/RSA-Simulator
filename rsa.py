def gcd(a, b):
    while b!=0:
        r=a%b
        a = b
        b = r
    return a

#Kiểm tra gcd
print(gcd(17, 3120))
print(gcd(12, 18))
print(gcd(25, 10))