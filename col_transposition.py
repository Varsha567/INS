
import math

def encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    rows = math.ceil(len(text) / cols)

    matrix = [["" for _ in range(cols)]
              for _ in range(rows)]

    index = 0
    for i in range(rows):
        for j in range(cols):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1

    cipher = ""

    for digit in key:
        col = int(digit) - 1
        for i in range(rows):
            if matrix[i][col] != "":
                cipher += matrix[i][col]

    return cipher


def decrypt(cipher, key):
    cols = len(key)
    rows = math.ceil(len(cipher) / cols)

    matrix = [["" for _ in range(cols)]
              for _ in range(rows)]

    index = 0

    for digit in key:
        col = int(digit) - 1
        for i in range(rows):
            if index < len(cipher):
                matrix[i][col] = cipher[index]
                index += 1

    text = ""
    for i in range(rows):
        for j in range(cols):
            text += matrix[i][j]

    return text


text = input("Enter Plain Text: ")
key = input("Enter Key: ")

cipher = encrypt(text, key)
decrypted = decrypt(cipher, key)

print("Encrypted Text:", cipher)
print("Decrypted Text:", decrypted)