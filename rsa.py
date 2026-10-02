from math import gcd

# Keys
p, q = 3, 11
n = p * q
phi = (p - 1) * (q - 1)

e = 3
while gcd(e, phi) != 1:
    e += 2

d = pow(e, -1, phi)

# Input
m = int(input("Enter message (number): "))

# Encryption and decryption
c = pow(m, e, n)
print("Encrypted:", c)

decrypted = pow(c, d, n)
print("Decrypted:", decrypted)