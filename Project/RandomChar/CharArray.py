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
