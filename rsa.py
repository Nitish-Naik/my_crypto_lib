"""using lib"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(public_key, plain_text):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    cipher_text = cipher.encrypt(plain_text.encode('utf-8'))
    return cipher_text

def rsa_decrypt(private_key, cipher_text):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_text = cipher.decrypt(cipher_text)
    return decrypted_text.decode('utf-8')

private_key, public_key = generate_rsa_keys()

message = input("Enter a plain text: ")
print("Plaintext:", message)

encrypted_message = rsa_encrypt(public_key, message)
print("Ciphertext:", encrypted_message)

decrypted_message = rsa_decrypt(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)












"""without lib"""

import math


def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp


p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)

while (e < phi):

    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1



k = 2
d = (1 + (k*phi))/e

msg = 12.0

print("Message data = ", msg)

c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)

m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)
