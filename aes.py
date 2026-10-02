from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=256)

aes = AESGCM(key)

nonce = os.urandom(12)

data = b"Hello, AES!"

ciphertext = aes.encrypt(nonce, data, None)

plaintext = aes.decrypt(nonce, ciphertext, None)

print("Cipher Text:", ciphertext)
print("Decrypted Text:", plaintext)