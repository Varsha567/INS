import numpy as np
from sympy import Matrix

def hill(text, key):
    text = text.upper().replace(" ", "")

    while len(text) % 3 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 3):
        block = [ord(c)-65 for c in text[i:i+3]]

        for row in key:
            value = sum(row[j]*block[j] for j in range(3))
            result += chr(value % 26 + 65)

    return result


def decrypt(text, key):
    inv = Matrix(key).inv_mod(26)
    inv = np.array(inv).astype(int).tolist()

    return hill(text, inv)


key = [[6,24,1],
       [13,16,10],
       [20,17,15]]

text = input("Enter plaintext: ")

enc = hill(text, key)
print("Encrypted:", enc)

dec = decrypt(enc, key)
print("Decrypted:", dec)




