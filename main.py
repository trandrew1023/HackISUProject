from Crypto.Cipher import AES
import pad

crypt_suite = AES.new('This is a keeeeeey1232eewwssdazZ', AES.MODE_CBC, 'This is an IV124')
cipher_text = crypt_suite.encrypt("SECRET MESSAGE DO NOT READ PADDD")
print(cipher_text)

decryption_suite = AES.new('This is a keeeeeey1232eewwssdazZ', AES.MODE_CBC, 'This is an IV124')
plain_text = decryption_suite.decrypt(cipher_text)

print(plain_text)

with open("secret.txt", 'r') as file, open("key.txt", 'r') as key, open("IV.txt", 'r') as IV:
    data = file.read()
    length = len(data)
    print("Data length " + str(length))
    mod = length % 16
    for x in range(0, mod):
        data += ' '
    length = len(data)
    print("Data length " + str(length))
    print(data)

    keyStr = key.read()
    IVstr = IV.read()
    
    padder = pad.pad_key(keyStr)
    data = pad.pad_data(data)
    lock = AES.new(padder, AES.MODE_CBC, IVstr)
    cipher = lock.encrypt(data)

    print(cipher)

    unlock = AES.new(padder, AES.MODE_CBC, IVstr)
    plain = unlock.decrypt(cipher)
    
    print(plain)


