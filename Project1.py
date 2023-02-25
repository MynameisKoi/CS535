# substitution cipher using Python
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "efghijklmnopqrstuvwxyzabcd"

# encrypt plaintext to cipher text
def encrypt(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            ciphertext += key[alphabet.index(char)]
        else:
            ciphertext += char
    return ciphertext

# decrypt cipher text to plaintext
def decrypt(ciphertext):
    plaintext = ""
    for char in ciphertext:
        if char in key:
            plaintext += alphabet[key.index(char)]
        else:
            plaintext += char
    return plaintext

# main function
plaintext = "ilovesfbu"
ciphertext = encrypt(plaintext)
print("plaintext: " + plaintext)
print("ciphertext: " + ciphertext)
print("decrypted: " + decrypt(ciphertext))

