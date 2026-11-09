def caesar_cipher(text, shift, mode="encrypt"):
  result = ""

 
  for char in text:

    if char.isalpha():

      if char.isupper():
        base = ord("A")  
      else:
        base = ord("a")  
      if mode == "encrypt":
        s = shift 
      else:
        s = -shift  
      shifted_index = (ord(char) - base + s) % 26
      new_char = chr(shifted_index + base)

      result += new_char

    else:
     
      result += char

  return result

encrypted = caesar_cipher("HELLO VIVA", 3, "encrypt")
print("Encrypted:", encrypted)  # Output: KHOOR YLYD

decrypted = caesar_cipher(encrypted, 3, "decrypt")
print("Decrypted:", decrypted)  # Output: HELLO VIVA


    