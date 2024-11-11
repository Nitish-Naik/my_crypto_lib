from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)
iv = get_random_bytes(16)

def aes_encrypt(plain_text):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    return cipher_text

def aes_decrypt(cipher_text):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size).decode('utf-8')
    return plain_text

plain_text = input("Enter a text: ")
print("Original message:", plain_text)

cipher_text = aes_encrypt(plain_text)
print("Encrypted message:", cipher_text)

decrypted_text = aes_decrypt(cipher_text)
print("Decrypted message:", decrypted_text)







def encrypt_caesar(plaintext, shift):
    encrypted = []
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted.append(encrypted_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)

# decrypt
def decrypt_caesar(ciphertext, shift):
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)


plaintext = input("Enter plaintext: ")
shift = 3  

encrypted_text = encrypt_caesar(plaintext, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt_caesar(encrypted_text, shift)
print("Decrypted text:", decrypted_text)



"""easiest deffie"""

def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

def main():

    P = 23
    print("The value of P:", P)


    G = 9
    print("The value of G:", G)


    a = 4
    print("The private key a for Alice:", a)

 
    x = power(G, a, P)

    b = 3
    print("The private key b for Bob:", b)

    y = power(G, b, P)

    ka = power(y, a, P)  
    kb = power(x, b, P)  

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

if __name__ == "__main__":
    main()










"""Pran"""

import random
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result
def diffie_hellman(p, g):
    private_key_A = int(input("Enter Alice's private key: "))
    private_key_B = int(input("Enter Bob's private key: "))
    public_key_A = mod_exp(g, private_key_A, p)
    public_key_B = mod_exp(g, private_key_B, p)
    shared_secret_A = mod_exp(public_key_B, private_key_A, p)
    shared_secret_B = mod_exp(public_key_A, private_key_B, p)
    if shared_secret_A == shared_secret_B:
        return shared_secret_A
    else:
        return "Error: Shared secrets do not match!"
p = int(input("Enter a prime number (p): ")) 
g = int(input("Enter a base (g): "))
shared_secret = diffie_hellman(p, g)
if shared_secret == "Error: Shared secrets do not match!":
    print(shared_secret)
else:
    print(f"Shared Secret: {shared_secret}")



"""Nit"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
import os

# Generate parameters for Diffie-Hellman
parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

# Alice generates her private key
alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()

# Bob generates his private key
bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()

# Alice and Bob exchange public keys
# Alice computes the shared key using Bob's public key
alice_shared_key = alice_private_key.exchange(bob_public_key)

# Bob computes the shared key using Alice's public key
bob_shared_key = bob_private_key.exchange(alice_public_key)

# Ensure both shared keys are the same
assert alice_shared_key == bob_shared_key

# Optionally, derive a key from the shared key for encryption
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Derive a key using the shared key
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=os.urandom(16),
    iterations=100000,
    backend=default_backend()
)

key = kdf.derive(alice_shared_key)

print("Alice's Public Key:", alice_public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
print("Bob's Public Key:", bob_public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
print("Derived Shared Key:", key.hex())





from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_DES(key, message):
    des = DES.new(key, DES.MODE_ECB)
    padded_message = pad(message)
    encrypted_message = des.encrypt(padded_message.encode('utf-8'))
    return binascii.hexlify(encrypted_message).decode('utf-8')

def decrypt_DES(key, encrypted_message):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_message = des.decrypt(binascii.unhexlify(encrypted_message))
    return decrypted_message.decode('utf-8').rstrip()

if __name__ == '__main__':
    key = get_random_bytes(8)
    message = input("Enter a message: ")
    print(f"Original Message: {message}")
    
    encrypted_message = encrypt_DES(key, message)
    print(f"Encrypted Message (Hex): {encrypted_message}")
    
    decrypted_message = decrypt_DES(key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")



from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization, hashes

def generate_keys():
    private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(message, hashes.SHA256())
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message, hashes.SHA256())
        return True
    except Exception:
        return False

if __name__ == "__main__":
    message = input("Enter the message to sign: ").encode('utf-8')
    
    private_key, public_key = generate_keys()
    signature = sign_message(private_key, message)
    
    print("Message:", message.decode())
    print("Signature:", signature.hex())

    # Verify the signature
    is_valid = verify_signature(public_key, message, signature)
    print("Signature valid:", is_valid)






