print('         ©2019 Ski Resort ZaharBerkut ')
print('############################################')
print('# The program generates a database')
print('# of codes for LOT turnstiles')
print('############################################\n')
import os
import binascii
import crcmod.predefined
import re

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False
x = int(input('Select positional system(1-DEC 2-HEX) '))

for case in switch(x):
    if case(1):
        vardec = input("DecNumber: ")
        range1 = input("Count: ")
        print()
        f = open("database.txt","w+")
        vardec10 = int(vardec)
        for i in range(vardec10, vardec10+int(range1)):
            crc8 = crcmod.predefined.Crc('crc-8-maxim')
            strdecData = str(i)
            decData = binascii.unhexlify(strdecData)
            crc8.update(decData)
            result = hex(crc8.crcValue)
            result = (result)[2:].zfill(2)
            print(strdecData + result)
            f.write(strdecData + result + '\n')
        break
    if case(2):
        varhex = input("HexNumber: ")
        range1 = input("Count: ")
        print()
        f = open("database.txt","w+")
        varhex16 = int(varhex, 16);
        for i in range(varhex16, varhex16+int(range1)):
            crc8 = crcmod.predefined.Crc('crc-8-maxim')
            strHexValPart = str(hex(i))[2:12]
            hexData = binascii.unhexlify(strHexValPart)
            crc8.update(hexData)
            result = hex(crc8.crcValue)
            result = (result)[2:].zfill(2)
            print(strHexValPart + result)
            f.write(strHexValPart + result + '\n')
        break
f.close()
print('')
print('Generated ' + str(range1) + ' codes')
input()
