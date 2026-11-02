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


# Tao mot so nguyen to ngau nhien
def generate_prime(min_value=100, max_value=500):
    if min_value < 2 or min_value > max_value:
        raise ValueError("Khoang gia tri khong hop le")

    while True:
        number = random.randint(min_value, max_value)

        if is_prime(number):
            return number


# Thuat toan Euclid mo rong
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd_value, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd_value, x, y


# Tim nghich dao modulo
def mod_inverse(e, phi):
    gcd_value, x, y = extended_gcd(e, phi)

    if gcd_value != 1:
        raise ValueError("e va phi phai nguyen to cung nhau")

    return x % phi


# Tinh luy thua modulo
def mod_pow(base, exponent, modulus):
    if modulus <= 0:
        raise ValueError("Modulus phai lon hon 0")

    if exponent < 0:
        raise ValueError("Exponent khong duoc am")

    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus

        base = (base * base) % modulus
        exponent = exponent // 2

    return result


# Tao khoa public va private
def generate_keys():
    p = generate_prime()
    q = generate_prime()

    while p == q:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    # Chon e sao cho gcd(e, phi) = 1
    e = 17
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 2

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


# Ma hoa thong diep
def encrypt(message, public_key):
    e, n = public_key

    if not isinstance(message, str):
        raise TypeError("Thong diep phai la chuoi")

    if n <= 255:
        raise ValueError("n phai lon hon 255 de ma hoa tung byte")

    # Doi chuoi thanh cac byte UTF-8 de ho tro tieng Viet
    message_bytes = message.encode("utf-8")
    encrypted_message = []

    for value in message_bytes:
        encrypted_value = mod_pow(value, e, n)
        encrypted_message.append(encrypted_value)

    return encrypted_message


# Giai ma thong diep
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_bytes = []

    for value in encrypted_message:
        if not isinstance(value, int) or value < 0 or value >= n:
            raise ValueError("Ban ma khong hop le")

        decrypted_value = mod_pow(value, d, n)

        if decrypted_value > 255:
            raise ValueError("Gia tri giai ma khong phai byte hop le")

        decrypted_bytes.append(decrypted_value)

    return bytes(decrypted_bytes).decode("utf-8")


if __name__ == "__main__":
    public_key, private_key = generate_keys()

    message = "Xin chao RSA"

    print("Public Key:", public_key)
    print("Private Key:", private_key)
    print("Thong diep goc:", message)

    encrypted_message = encrypt(message, public_key)
    print("Thong diep da ma hoa:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Thong diep sau giai ma:", decrypted_message)
