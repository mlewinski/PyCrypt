# -*- coding: utf-8 -*-
def Encrypt(alphabet, message, key):
    ciphertext = ""
    
    for x in message:
        if x in alphabet:
            ciphertext += alphabet[(alphabet.index(x)+key)%alphabet.__len__()]
        else:
            ciphertext += x
    
    return ciphertext
    
def Decrypt(alphabet, ciphertext, key):
    message = ""
    
    for x in ciphertext:
        if x in alphabet:
            message += alphabet[(alphabet.index(x)-key)%alphabet.__len__()]
        else:
            message += x
    
    return message