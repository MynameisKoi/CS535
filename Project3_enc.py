import hashlib
import os
from cryptography.fernet import Fernet
# Generate a random number
random_number = os.urandom(16)
# Hash the random number using SHA-256
hash_object = hashlib.sha256()
hash_object.update(random_number)
message_digest = hash_object.digest()
# Generate a Fernet key
session_key = Fernet.generate_key()
# Create a Fernet cipher suite with the session key
cipher_suite = Fernet(session_key)
# Encrypt the random number and message digest using the cipher suite
data_to_encrypt = random_number + message_digest
encrypted_data = cipher_suite.encrypt(data_to_encrypt)
print("Random Number:", random_number)
print("Message Digest:", message_digest)
print("Session Key:", session_key)
print("Encrypted Data:", encrypted_data)