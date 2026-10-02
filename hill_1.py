def hill(text, key):
    text = "".join(c for c in text.upper() if c.isalpha())

    while len(text) % 3:
        text += "X"

    result = ""

    for i in range(0, len(text), 3):
        block = [ord(c) - 65 for c in text[i:i+3]]

        for row in key:
            value = sum(row[j] * block[j] for j in range(3))
            result += chr(value % 26 + 65)

    return result


key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

text = input("Enter plaintext: ")
cipher = hill(text, key)

print("Encrypted:", cipher)