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