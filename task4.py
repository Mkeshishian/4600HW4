from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import rsa

def sign_messages():
    # Public and private keys
    e = 65537
    n = 226582599423272186758101375008313514163
    d = 10520163231270616538808580112244880993

    # Original message
    message1 = "I owe you $2000."

    # Modified message
    message2 = "I owe you $3000."

    # Convert messages to bytes
    message1_bytes = message1.encode()
    message2_bytes = message2.encode()

    # Load private key
    key = RSA.construct((n, e, d))

    # Sign the original message
    h1 = SHA256.new(message1_bytes)
    signature1 = rsa.sign(message1_bytes, key.export_key(), 'SHA-256')

    # Sign the modified message
    h2 = SHA256.new(message2_bytes)
    signature2 = rsa.sign(message2_bytes, key.export_key(), 'SHA-256')

    # Print signatures
    print("Signature 1:", signature1.hex())
    print("Signature 2:", signature2.hex())
sign_messages()
