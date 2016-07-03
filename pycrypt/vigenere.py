# -*- coding: utf-8 -*-
from pycrypt import caesar

def Encrypt(alphabet, message, key):
    ciphertext = ""
    keyCounter = 0
    for x in range(0, len(message)):
        ciphertext += caesar.Encrypt(alphabet, message[x], alphabet.index(key[keyCounter]))
        keyCounter+=1
        if keyCounter == len(key): keyCounter=0
    return ciphertext
    
def Decrypt(alphabet, ciphertext, key):
    message = ""
    keyCounter = 0
    for x in range(0, len(ciphertext)):
        if keyCounter == len(key): keyCounter=0
        message += caesar.Decrypt(alphabet, ciphertext[x],  alphabet.index(key[keyCounter]))
        keyCounter+=1
        if keyCounter == len(key): keyCounter=0
    return message