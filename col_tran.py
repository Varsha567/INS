
def encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)

    table = {int(k): "" for k in key}

    for i, ch in enumerate(text):
        col = i % cols
        table[int(key[col])] += ch

    cipher = ""

    for k in sorted(table):
        cipher += table[k]

    return cipher


def decrypt(cipher, key):
    cols = len(key)
    n = len(cipher)

    # Number of characters in each column
    lengths = [n // cols] * cols

    for i in range(n % cols):
        lengths[i] += 1

    table = {int(k): "" for k in key}
    index = 0

    # Fill columns in sorted key order
    for i in sorted(range(cols), key=lambda x: int(key[x])):
        col = int(key[i])
        table[col] = cipher[index:index + lengths[i]]
        index += lengths[i]

    # Read row-wise
    plain = ""

    for row in range(max(lengths)):
        for k in key:
            col = int(k)
            if row < len(table[col]):
                plain += table[col][row]

    return plain


text = input("Enter Plain Text: ")
key = input("Enter Key: ")

cipher = encrypt(text, key)

print("Encrypted Text:", cipher)
print("Decrypted Text:", decrypt(cipher, key))
