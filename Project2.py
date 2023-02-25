def KSA(key):
    # Key-Scheduling Algorithm (KSA)
    S = list(range(256))
    # initialize T array with key and size S
    T = [ord(key[i % len(key)]) for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap values
    return S

def PRGA(S):
    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap values
        t = (S[i] + S[j]) % 256
        K = S[t]
        yield K

def RC4(key, plaintext):
    S = KSA(key)
    keystream = PRGA(S)
    return bytes([next(keystream) for _ in range(len(plaintext))])

# Step 1: Generate RC4 Keystream
key = 'brucelee'
plaintext = b'attackatdawn'
keystream = RC4(key, plaintext)
print("Keystream:", keystream)

# Step 2: Encrypt plaintext using Stream Cipher
ciphertext = bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])
print("Ciphertext:", ciphertext)

# Step 3: Decrypt ciphertext using Stream Cipher
decrypted_plaintext = bytes([ciphertext[i] ^ keystream[i] for i in range(len(ciphertext))])
print("Decrypted plaintext:", decrypted_plaintext.decode())

