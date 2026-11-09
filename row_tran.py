
def encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)

    table = [""] * cols

    for i, ch in enumerate(text):
        table[i % cols] += ch

    cipher = ""

    for k in key:
        cipher += table[int(k) - 1]

    return cipher


def decrypt(cipher, key):
    cols = len(key)
    n = len(cipher)

    # Number of characters in each column
    lengths = [n // cols] * cols

    for i in range(n % cols):
        lengths[i] += 1

    table = [""] * cols
    index = 0

    for k in key:
        col = int(k) - 1
        table[col] = cipher[index:index + lengths[col]]
        index += lengths[col]

    plain = ""

    for row in range(max(lengths)):
        for col in range(cols):
            if row < len(table[col]):
                plain += table[col][row]

    return plain


text = input("Enter Plain Text: ")
key = input("Enter Key: ")

cipher = encrypt(text, key)

print("Encrypted Text:", cipher)
print("Decrypted Text:", decrypt(cipher, key))

