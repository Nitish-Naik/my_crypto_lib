"""using lib"""

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
