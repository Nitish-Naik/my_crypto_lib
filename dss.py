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
