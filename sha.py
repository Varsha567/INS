import hashlib
def generate_sha256(message: str):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode('utf-8'))
    return sha256_hash.hexdigest()
input_message = "Hello, Cryptography!"
print("Input:", input_message)
print("SHA-256 Output:", generate_sha256(input_message))