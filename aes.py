from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
key=b"1234567890123456"
cipher=AES.new(key, AES.MODE_ECB)
plaintext=input("Enter text: ")
encrypted=cipher.encrypt(pad(plaintext.encode(), AES.block_size))
print("Encrypted text:", encrypted.hex())
decipher=AES.new(key, AES.MODE_ECB)
decrypted=unpad(decipher.decrypt(encrypted), AES.block_size)
print("Decrpted Text:", decrypted.decode())