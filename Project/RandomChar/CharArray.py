import random


# Adds the random characters to the two strings str16 and str32.
class AddChar:
    str16 = ""
    str32 = ""

    def __init__(self):
        self

    def addchar(self, char):
        if (char > 0x1F) and (char < 0x7F):
            if len(self.str16) <= 16:
                self.str16 = "" + self.str16 + chr(char)
            elif len(self.str32) <= 32:
                self.str32 = "" + self.str32 + chr(char)

    def get16(self):
        return self.str16

    def get32(self):
        return self.str32


# For testing purposes only.
i = 0
j = 0
temp = AddChar()
while len(temp.get16()) <= 16:
    temp.addchar(random.randint(0, 255))

while len(temp.get32()) <= 32:
    temp.addchar(random.randint(0, 255))

print(temp.get16())
print(temp.get32())