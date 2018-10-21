import os
import crypt
import pad
PATH_A = "./driveA"
PATH_B = "./driveB"

FILE_PICS = "./cats"
KEY_PICS = "./dogs"

counter = 0

key = "This is a placeholder"
iv = "also a placehold"

key = pad.pad_key(key)

tex = crypt.encrypt("Hello world", key, iv)
print(tex)

tex = crypt.decrypt(tex, key)
print(tex)

fo = open("./driveA/secret1.txt", "r")
tex = fo.read()
print(tex)
fo.close()    
tex = crypt.encrypt(tex, key, iv)
print(tex)
fo = open("./driveA/secret1.enc", "w")
fo.write(str(tex))
fo.close()
os.system("steghide embed -ef ./driveA/secret1.enc -cf ./dogs/dog01.jpg -p dog01 -sf ./driveA/dog01.jpg")
