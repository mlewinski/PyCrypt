# -*- coding: utf-8 -*-
from pycrypt import caesar

message = input("Message : ")
key = int(input("Key : "))

ciphertext = caesar.Encrypt("abcdefghijklmnopqrstuwvxyz0123456789", message, key)

print(ciphertext)

print(caesar.Decrypt("abcdefghijklmnopqrstuwvxyz0123456789", ciphertext, key))

