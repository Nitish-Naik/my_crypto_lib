aes = '''from Crypto.Cipher import AES
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
'''


caesar = '''
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
print("Decrypted text:", decrypted_text)'''




deffie = '''"""easiest deffie"""

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
print("Derived Shared Key:", key.hex())'''



des = '''from Crypto.Cipher import DES
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
'''

dss='''from cryptography.hazmat.backends import default_backend
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
'''





hill = '''

keyMatrix = [[0] * 3 for i in range(3)]


messageVector = [[0] for i in range(3)]

cipherMatrix = [[0] for i in range(3)]

def getKeyMatrix(key):
	k = 0
	for i in range(3):
		for j in range(3):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1

def encrypt(messageVector):
	for i in range(3):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(3):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):


	getKeyMatrix(key)

	for i in range(3):
		messageVector[i][0] = ord(message[i]) % 65


	encrypt(messageVector)

	CipherText = []
	for i in range(3):
		CipherText.append(chr(cipherMatrix[i][0] + 65))

	print("Ciphertext: ", "".join(CipherText))


def main():
	message = "ACT"


	key = "GYBNQKURP"

	HillCipher(message, key)

if __name__ == "__main__":
	main()


'''



ids = '''
"""


PROCEDURE:
Prerequisites: Snort should be installed on a Linux machine. If it's not
installed, you can do so with:
```bash
sudo apt-get update
sudo apt-get install snort
```
Step 1: Configure Snort in promiscuous mode
Make sure your network interface is set to promiscuous mode to capture all
network traffic. For example:
```bash
sudo ip link set eth0 promisc on
```
Replace `eth0` with the appropriate network interface on your machine.
Step 2: Writing a basic Snort rule
Create a custom Snort rule to detect specific malicious activity. Let's say you
want to detect ICMP Ping (Echo Requests):
1. Open the rules file, usually located at `/etc/snort/rules/local.rules`:
```bash
sudo nano /etc/snort/rules/local.rules
```
2. Add the following rule to detect an ICMP ping request (commonly
used in ping sweeps):
```plaintext
alert icmp any any -> any any (msg:"ICMP Ping detected";
itype:8; sid:1000001; rev:1;)
```
Explanation:
- `alert` – defines the action to be taken when the rule matches.
- `icmp` – protocol type.
- `any any -> any any` – matches traffic from any IP and port to any IP and
port.
- `msg:"ICMP Ping detected"` – the alert message that will be logged.
- `itype:8` – filters for ICMP echo requests (ping).
- `sid:1000001` – unique Snort rule ID. 




- `rev:1` – rule revision number.
 Step 3: Run Snort in NIDS mode
```bash
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
```
- `-A console` – outputs alerts to the console.
- `-q` – runs Snort in quiet mode to reduce non-essential output.
- `-c` – specifies the configuration file.
- `-i eth0` – sets the interface Snort will listen to (replace `eth0` with your
network interface).`
 Step 4: Test the IDS
```bash
ping <target-ip>
```
If Snort detects the ICMP ping request, it will generate an alert in the console
that matches the rule you defined.
 Example Output:
If the ping is detected, Snort will output something like:
```plaintext
[**] [1:1000001:1] ICMP Ping detected [**] 
"""'''





md5 = '''"""using lib"""

import hashlib


def compute_md5(input_data):
    
    md5_hash = hashlib.md5()
    
    
    md5_hash.update(input_data)
    

    return md5_hash.hexdigest()


if __name__ == "__main__":
    input_data = b"Hello, world!"
    hash_result = compute_md5(input_data)
    print("MD5:", hash_result)
    
    
    
    
    
"""without lib"""



import struct

S = [7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21]
K = [int(abs(struct.unpack('!I', struct.pack('!I', i))[0]) * 2**32) % 2**32 for i in range(1, 65)]

def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md5(message):
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    message += b'\x00' * ((56 - (original_byte_len + 1) % 64) % 64)
    message += struct.pack('<Q', original_bit_len)
    a, b, c, d = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        w = list(struct.unpack('<16L', chunk)) + [0] * 48
        for j in range(64):
            if 0 <= j <= 15:
                f, g = (b & c) | (~b & d), j
            elif 16 <= j <= 31:
                f, g = (d & b) | (~d & c), (5 * j + 1) % 16
            elif 32 <= j <= 47:
                f, g = b ^ c ^ d, (3 * j + 5) % 16
            else:
                f, g = c ^ (b | ~d), (7 * j) % 16
            f = (f + a + K[j] + w[g]) & 0xFFFFFFFF
            a, d, c, b = d, (b + left_rotate(f, S[j % 4 + (j // 16) * 4])) & 0xFFFFFFFF, b, c
        a = (a + 0x67452301) & 0xFFFFFFFF
        b = (b + 0xEFCDAB89) & 0xFFFFFFFF
        c = (c + 0x98BADCFE) & 0xFFFFFFFF
        d = (d + 0x10325476) & 0xFFFFFFFF
    return struct.pack('<4L', a, b, c, d)

def md5_hexdigest(message):
    return ''.join(f'{byte:02x}' for byte in md5(message))

if __name__ == "__main__":
    input_data = b"Hello, world!"
    print("MD5:", md5_hexdigest(input_data))
'''



playfair = '''
def toLowerCase(text):
    return text.lower()



def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText




def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])

        group = i
    Diagraph.append(text[group:])
    return Diagraph




def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix


def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]

    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]

    return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]

    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]

    return char1, char2


def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2


def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText


text_Plain = 'instruments'
text_Plain = removeSpaces(toLowerCase(text_Plain))
PlainTextList = Diagraph(FillerLetter(text_Plain))
if len(PlainTextList[-1]) != 2:
    PlainTextList[-1] = PlainTextList[-1]+'z'

key = "Monarchy"
print("Key text:", key)
key = toLowerCase(key)
Matrix = generateKeyTable(key, list1)

print("Plain Text:", text_Plain)
CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

CipherText = ""
for i in CipherList:
    CipherText += i
print("CipherText:", CipherText)'''

railfence = '''def encryptRailFence(text, key):
	rail = [['\n' for i in range(len(text))] for j in range(key)]
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)):
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down
		rail[row][col] = text[i]
		col += 1
		if dir_down:
			row += 1
		else:
			row -= 1
	
	result = []
	for i in range(key):
		for j in range(len(text)):
			if rail[i][j] != '\n':
				result.append(rail[i][j])
	return "".join(result)
	
def decryptRailFence(cipher, key):
	rail = [['\n' for i in range(len(cipher))] for j in range(key)]
	dir_down = None
	row, col = 0, 0
	
	for i in range(len(cipher)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False
		rail[row][col] = '*'
		col += 1
		if dir_down:
			row += 1
		else:
			row -= 1
	
	index = 0
	for i in range(key):
		for j in range(len(cipher)):
			if rail[i][j] == '*' and index < len(cipher):
				rail[i][j] = cipher[index]
				index += 1
	
	result = []
	row, col = 0, 0
	for i in range(len(cipher)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False
		if rail[row][col] != '*':
			result.append(rail[row][col])
			col += 1
		if dir_down:
			row += 1
		else:
			row -= 1
	return "".join(result)

if __name__ == "__main__":
	print(encryptRailFence("attack at once", 2))
	print(encryptRailFence("GeeksforGeeks ", 3))
	print(encryptRailFence("defend the east wall", 3))
	print(decryptRailFence("GsGsekfrek eoe", 3))
	print(decryptRailFence("atc toctaka ne", 2))
	print(decryptRailFence("dnhaweedtees alf tl", 3))
'''

rsa = '''"""using lib"""

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

'''

sha='''import hashlib

def sha512_hash(input_string):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(input_string.encode('utf-8'))
    return sha512_hash.hexdigest()


input_string = input("Enter input : ")
print(sha512_hash(input_string))
'''

vigenere = '''def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

text_to_encrypt = "HelloWorld"
key = "KEY"

encrypted_text = encrypt_vigenere(text_to_encrypt, key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt_vigenere(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")


'''

def get_cipher_by_number():
    cipher_map = {
        1: "aes",
        2: "caesar",
        3: "deffie",
        4: "des",
        5: "dss",
        6: "ids",
        7: "hill",
        8: "md5",
        9: "playfair",
        10: "railfence",
        11: "sha",
        12: "vigenere"
    }
    lst = list(cipher_map.values())
    print(hill)

get_cipher_by_number()
