#ước chung lớn nhất
def gcd(a, b):
    while b!=0:
        r =a %b 
        a = b
        b = r
    return a

#Kiểm tra gcd
print(gcd(17, 3120))
print(gcd(12, 18))
print(gcd(25, 10))

#số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i<= n:
        if n % i == 0:
            return False
        i += 1
    return True

#Kiểm tra is_prime
print(is_prime(7))
print(is_prime(13))
print(is_prime(15))
print(is_prime(1))