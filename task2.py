from Crypto.Util.number import *
import binascii

# Public key
e = 65537
n = 226582599423272186758101375008313514163

# Convert message to bytes and then to hex
message = "A top secret!"
message_bytes = message.encode('utf-8')
message_hex = binascii.hexlify(message_bytes).decode('utf-8')

# Convert hex string to integer
m = int(message_hex, 16)

# Encrypt using the public key
c = pow(m, e, n)

# Convert ciphertext to hex string
ciphertext_hex = hex(c)[2:]

# Print ciphertext
print("Ciphertext:", ciphertext_hex)

