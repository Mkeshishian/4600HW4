from Crypto.Util.number import *
import binascii

# Define function to encrypt message using RSA
def encrypt(message, e, n):
    # Convert message to hex string
    message_hex = binascii.hexlify(message.encode()).decode()

    # Convert hex string to BIGNUM
    m = int(message_hex, 16)

    # Encrypt using the public key
    c = pow(m, e, n)

    # Return ciphertext
    return c

# Public key
e = 65537
n = 0xDCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5

# Message to encrypt
message = "A top secret!"

# Encrypt message using RSA
ciphertext = encrypt(message, e, n)

# Print ciphertext
print("Ciphertext:", hex(ciphertext))
