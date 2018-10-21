import random
import secrets
import string
from Crypto.Cipher import AES
def pad_key(data):
    diff = 32 - len(data)
    if diff > 0:
        for x in range(0, diff):
            data += str(secrets.choice(string.ascii_letters + string.punctuation + string.digits))
    return str(data[:32])

def pad_data(data):
    #return data + b"\0" * (AES.block_size - len(data) % AES.block_size) 
    mod = len(data) % 16
    for x in range(0, (16 - mod)):
        data += "\0"
    return data


def pad_iv(iv):
    diff = 16 - len(iv)
    if diff > 0:
        for x in range(0, diff):
            iv += str(secrets.choice(string.ascii_letters + string.punctuation + string.digits))
    return iv[:16]
