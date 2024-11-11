
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