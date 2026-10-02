from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad 

key = b"12345678"

cipher = DES.new(key, DES.MODE_ECB)

plaintext = "Hello DES"

encrypted = cipher.encrypt(pad(plaintext.encode(), DES.block_size))

decipher = DES.new(key, DES.MODE_ECB)

decrypted = unpad(decipher.decrypt(encrypted), DES.block_size)

print("Encrypted:", encrypted.hex())
print("Decrypted:", decrypted.decode())