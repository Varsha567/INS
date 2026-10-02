
def generate_key_table(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    seen = set()
    table = []

    for ch in key + alphabet:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            table.append(ch)

    return [table[i:i + 5] for i in range(0, 25, 5)]


def find_position(table, ch):
    if ch == "J":
        ch = "I"

    for i in range(5):
        for j in range(5):
            if table[i][j] == ch:
                return i, j


def prepare_text(text):
    text = ''.join(filter(str.isalpha, text.upper()))
    text = text.replace("J", "I")

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]

            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "X"
            i += 1

    return result


def encrypt(text, key):
    table = generate_key_table(key)
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = find_position(table, a)
        r2, c2 = find_position(table, b)

        if r1 == r2:
            cipher += table[r1][(c1 + 1) % 5]
            cipher += table[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher += table[(r1 + 1) % 5][c1]
            cipher += table[(r2 + 1) % 5][c2]

        else:
            cipher += table[r1][c2]
            cipher += table[r2][c1]

    return cipher


def decrypt(cipher, key):
    table = generate_key_table(key)
    result = ""

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i + 1]
        r1, c1 = find_position(table, a)
        r2, c2 = find_position(table, b)

        if r1 == r2:
            result += table[r1][(c1 - 1) % 5]
            result += table[r2][(c2 - 1) % 5]

        elif c1 == c2:
            result += table[(r1 - 1) % 5][c1]
            result += table[(r2 - 1) % 5][c2]

        else:
            result += table[r1][c2]
            result += table[r2][c1]

    return result


text = input("Enter plaintext: ")
key = input("Enter key: ")

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)