import random


# Tim uoc chung lon nhat
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


# Kiem tra so nguyen to
def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


# Sinh mot so nguyen to ngau nhien
def generate_prime(min_value=100, max_value=500):
    while True:
        number = random.randint(min_value, max_value)

        if is_prime(number):
            return number


# Thuat toan Euclid mo rong
# Dung de tim gcd va cac he so x, y
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd_value, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd_value, x, y


# Tim nghich dao modulo
def mod_inverse(e, phi):
    gcd_value, x, _ = extended_gcd(e, phi)

    if gcd_value != 1:
        return None

    return x % phi


# Tu tinh luy thua modulo
# Tinh (base ^ exponent) % modulus
def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus

        exponent = exponent // 2
        base = (base * base) % modulus

    return result


# Sinh Public Key va Private Key
def generate_keys():
    p = generate_prime()
    q = generate_prime()

    # p va q phai khac nhau
    while p == q:
        q = generate_prime()

    # Tinh n
    n = p * q

    # Tinh phi(n)
    phi = (p - 1) * (q - 1)

    # Chon e sao cho gcd(e, phi) = 1
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Tim d
    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


# Ma hoa mot thong diep
def encrypt(message, public_key):
    e, n = public_key
    encrypted = []

    for char in message:
        number = ord(char)
        encrypted_number = mod_pow(number, e, n)
        encrypted.append(encrypted_number)

    return encrypted


# Giai ma ban ma
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted = ""

    for number in encrypted_message:
        decrypted_number = mod_pow(number, d, n)
        decrypted += chr(decrypted_number)

    return decrypted
