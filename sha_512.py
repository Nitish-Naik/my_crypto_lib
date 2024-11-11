import hashlib

def sha512_hash(input_string):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(input_string.encode('utf-8'))
    return sha512_hash.hexdigest()


input_string = input("Enter input : ")
print(sha512_hash(input_string))