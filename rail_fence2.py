def encrypt(text, key):
    rails = [[] for _ in range(key)]

    row = 0
    step = 1

    for ch in text:
        rails[row].append(ch)

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1

        row += step

    return "".join("".join(rail) for rail in rails)


def decrypt(cipher, key):
    pattern = []
    row = 0
    step = 1

    for _ in cipher:
        pattern.append(row)

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1

        row += step

    counts = [pattern.count(i) for i in range(key)]

    rails = []
    index = 0

    for count in counts:
        rails.append(list(cipher[index:index + count]))
        index += count

    result = ""

    for row in pattern:
        result += rails[row].pop(0)

    return result


text = input("Enter plaintext: ")
key = int(input("Enter number of rails: "))

cipher = encrypt(text, key)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, key))