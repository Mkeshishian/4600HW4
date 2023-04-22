from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import rsa

def verify_signature():
    # Public key
    e = 65537
    n = 151797541829575907036247533638534858562508603169596730498905763931327970671550058152864543505399205981011918181135398739191972196997308110221808372016753334020786204316840344932773739390480635071407760054934812252103404585563946333553766997357833814397931186225856393361197362117802278934381266051828443203259
    public_key = RSA.construct((n, e))

    # Message and signature
    message = "Launch a missile."
    signature_hex = "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F"
    signature = bytes.fromhex(signature_hex)

    # Verify the signature
    h = SHA256.new(message.encode())
    if rsa.verify(h.digest(), signature, public_key):
        print("Signature is valid.")
    else:
        print("Signature is invalid.")
verify_signature()
