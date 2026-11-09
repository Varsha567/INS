from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()
message = b"Digital Signature Standard"
signature = private_key.sign(
message,
hashes.SHA256())
print("Original Message:", message.decode())
print("Digital Signature:", signature.hex())
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256() )
    print("Signature Verification: SUCCESS")
    print("The message is authentic and has not been modified.")
except InvalidSignature:
    print("Signature Verification: FAILED")