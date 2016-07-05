# -*- coding: utf-8 -*-
from pycrypt import caesar
from pycrypt import vigenere
from pycrypt import railfence

print("Caesar:")

#message = input("Message : ")
#key = int(input("Key : "))

#ciphertext = caesar.Encrypt("abcdefghijklmnopqrstuwvxyz0123456789", message, key)

#print(ciphertext)

#print(caesar.Decrypt("abcdefghijklmnopqrstuwvxyz0123456789", ciphertext, key))

#print("Vigenere:")

#message = input("Message : ")
#key = input("Key : ")

#ciphertext = vigenere.Encrypt("abcdefghijklmnopqrstuwvxyz0123456789", message, key)

#print(ciphertext)

#print(vigenere.Decrypt("abcdefghijklmnopqrstuwvxyz0123456789", ciphertext, key))

message = input("Message : ")
key = int(input("Key : "))

ciphertext = railfence.Encrypt(message, key)

print(ciphertext)