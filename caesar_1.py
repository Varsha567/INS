def ceaser(text,s):
    result=""
    for ch in text:
        if ch.isupper():
            result+=chr((ord(ch)-65+s)%26+65)
        elif ch.islower():
            result+=chr((ord(ch)-97+s)%26+97)
        else:
            result+=ch
    return result # Added return statement

plain_text="hello"
s=3
ciper=ceaser(plain_text,s)
plain=ceaser(ciper,-s)
print(ciper)
print(plain)