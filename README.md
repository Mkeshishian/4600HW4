# 4600HW4 Michael Keshishian

# Task 1 C

I used C in Task 1. I used the RSA algorithm to determine the private key for a given public key.  I started by creating helper functions that compute the greatest common factor of two numbers, convert hexadecimal characters to byte arrays, and compute the modular inverse of a value. I then set several variables with the values p, q, and e to represent hexadecimal strings. I calculated n and phi using these values, and I then calculated the modular inverse of e and phi to obtain d.  Finally, I converted d to a hexadecimal string and printed out the results.


![image](https://user-images.githubusercontent.com/89661528/233740214-c9292fb1-cc9c-438a-9a3c-3ad812bbcbb7.png)

# Task 2 Python

I used Python for Task 2. This code uses the Crypto.Util.number and binascii modules to encrypt a message using RSA. The encrypt() function first converts the message to a hex string and then to a BIGNUM. It then encrypts the BIGNUM using the public key provided, e and n. The message to be encrypted is then defined, followed by the public key values e and n. These variables are used to call the encrypt() method, and hex() is used to output the ciphertext.


![image](https://user-images.githubusercontent.com/89661528/233752185-e2cf2f60-e37d-42c4-93b0-5d15313a3240.png)

# Task 3 Python

I used Python for Task 3. This code defines a function called decrypt_message that takes in a ciphertext as a hexadecimal string and uses RSA decryption to return the plaintext message. The function first initializes the public and private keys, converts the ciphertext from hexadecimal to an integer, then decrypts the ciphertext using the private key, then converts the decrypted integer to plaintext, and finally returns the plaintext message. The ciphertext is a hexadecimal string, and the code prints the final decrypted message.



![image](https://user-images.githubusercontent.com/89661528/233752415-b29c39e2-7479-4306-a33a-787d005374ac.png)

# Task 4 Python

I used Python for Task 4. This code defines a function to sign messages using RSA. It creates a public-private key pair, and two messages, one of which is modified ( “I owe you $2000” and  “I owe you $3000”). It then loads the private key, signs each message using the key and the SHA-256 hashing algorithm, and prints the resulting signatures.


![image](https://user-images.githubusercontent.com/89661528/233755254-d0517353-a353-4bbe-9d2a-146730d4b525.png)

# Task 5 Python

I used Python for Task 5. This code verifies a digital signature using an RSA public key. The code loads a public key, a message, and a signature, and then uses the RSA algorithm and the SHA256 hash function to verify the signature. If the signature is valid, the program prints "Signature is valid.". If it is not valid the program prints "Signature is invalid.".


![image](https://user-images.githubusercontent.com/89661528/233755545-a6d11e92-eade-42a6-ad6a-f6f242286a97.png)
