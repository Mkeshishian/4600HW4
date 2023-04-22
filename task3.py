from Crypto.Util.number import *

def decrypt_message(ciphertext_hex):
    # Public/Private keys
    n = 0xDCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
    e = 0x10001
    d = 0x74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D

    # Convert ciphertext from hex to int
    ciphertext = int(ciphertext_hex, 16)

    # Decrypt ciphertext using private key
    plaintext_int = pow(ciphertext, d, n)

    # Convert decrypted int to bytes and then to plain text
    plaintext_bytes = long_to_bytes(plaintext_int)
    plaintext = plaintext_bytes.decode()

    return plaintext

ciphertext_hex = "8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F"
plaintext = decrypt_message(ciphertext_hex)
print("Decrypted message:", plaintext)


