from cryptography.fernet import Fernet
import hashlib
# Encrypted data from the 'encrypt.py' output
encrypted_data = b'gAAAAABkN3GY52_eIJ7bgdHbZLq0foRbel41MAkSY8SsbjeTK6iLOlGZrkWvCR5tPKKJw25xqMVUMF9Qze1PO_hU1NKOf6G1zMpImE6bC1TOctOoEP3KjCVJAHTTS6cEZ2aYOS4W0kcx2DcTSM5SN6-muFJrbRR1WQ=='
# Session key from the 'encrypt.py' output
session_key =  b'ysef8pKBuPJlxbJbpk7ycAh01hpBAkshJETAnbUnhNg='
# Create a Fernet cipher suite with the session key
cipher_suite = Fernet(session_key)
# Decrypt the encrypted data using the cipher suite
decrypted_data = cipher_suite.decrypt(encrypted_data)
# Extract the random number and message digest from the decrypted data
decrypted_random_number = decrypted_data[:16]
decrypted_message_digest = decrypted_data[16:]
print("Decrypted Random Number:", decrypted_random_number)
print("Decrypted Message Digest:", decrypted_message_digest)
# Hash the random number using SHA-256
hash_object = hashlib.sha256()
hash_object.update(decrypted_random_number)
message_digest = hash_object.digest()
# Compare the decrypted random number and message digest with the original values
if decrypted_message_digest == message_digest:
    print("Decrypted message digest matches the message digest.")
else:
    print("Decrypted data does not match the original data.")