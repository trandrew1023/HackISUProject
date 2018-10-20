from Crypto.Cipher import AES
import pad
def encrypt(message, key, iv, key_size=256):
    message = pad.pad_data(message)
    iv = pad.pad_iv(iv)
    key = pad.pad_key(str(key))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv.encode() + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b'\0')

def encrypt_file(file_name, key, iv):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key, iv)
    print(str(len(enc)))
    return enc

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    return dec

with open("secret.txt", 'r') as fo:
    message = fo.read()
    print("Original message length: " + str(len(message)))
    message = pad.pad_data(message)
    print("Padded message length: " + str(len(message)))

with open("key.txt", 'r') as fo:
    key = fo.read()
    print("Original key length: " + str(len(key)))
    key = pad.pad_key(key)
    print("Padded key length: " + str(len(key)))

with open("IV.txt", 'r') as fo:
    iv = fo.read()
    print("Original IV length: " + str(len(iv)))
    iv = pad.pad_iv(iv)
    print("Padded IV length: " + str(len(iv)))

crypt = encrypt(message, key, iv)
print(crypt)

dec = decrypt(crypt, key)
print(dec)
