def generate_key(msg, key):
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

"""
public class Vigenere_cipher_java {

    public static String encrypt(String plaintext, String key) {
        String alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // Ensure plaintext and key are uppercase
        plaintext = plaintext.toUpperCase();
        key = key.toUpperCase();

        // Extend the key
        StringBuilder extendedKey = new StringBuilder(key);
        while (extendedKey.length() < plaintext.length()) {
            extendedKey.append(key);
        }
        extendedKey.setLength(plaintext.length());
        key = extendedKey.toString();

        // Encrypt the plaintext
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < plaintext.length(); i++) {
            char pChar = plaintext.charAt(i);
            char kChar = key.charAt(i);
            if (Character.isLetter(pChar)) {
                int pIndex = alphabets.indexOf(pChar);
                int kIndex = alphabets.indexOf(kChar);
                char encryptedChar = alphabets.charAt((pIndex + kIndex) % 26);
                sb.append(encryptedChar);
            } else {
                sb.append(pChar);
            }
        }
        return sb.toString();
    }

    public static String decrypt(String encryptedText, String key) {
        String alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // Ensure encryptedText and key are uppercase
        encryptedText = encryptedText.toUpperCase();
        key = key.toUpperCase();

        // Extend the key
        StringBuilder extendedKey = new StringBuilder(key);
        while (extendedKey.length() < encryptedText.length()) {
            extendedKey.append(key);
        }
        extendedKey.setLength(encryptedText.length());
        key = extendedKey.toString();

        // Decrypt the encrypted text
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < encryptedText.length(); i++) {
            char eChar = encryptedText.charAt(i);
            char kChar = key.charAt(i);
            if (Character.isLetter(eChar)) {
                int eIndex = alphabets.indexOf(eChar);
                int kIndex = alphabets.indexOf(kChar);
                // Adjust for negative result
                int decryptedIndex = (eIndex - kIndex + 26) % 26;
                char decryptedChar = alphabets.charAt(decryptedIndex);
                sb.append(decryptedChar);
            } else {
                sb.append(eChar);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String plaintext = "GEEKSFORGEEKS";
        String key = "ayush";

        String encryptedText = encrypt(plaintext, key);
        String decryptedText = decrypt(encryptedText, key);

        System.out.println("Encrypted text = " + encryptedText);
        System.out.println("Decrypted text = " + decryptedText);
    }
}

"""