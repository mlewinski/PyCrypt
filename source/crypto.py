# -*- coding: utf-8 -*-
import cryptolib

message = input("Message : ")
key = int(input("Key : "))

ciphertext = cryptolib.caesar.CaesarEncrypt("abcdefghijklmnopqrstuwvxyz0123456789", message, key)

print(ciphertext)

print(cryptolib.caesar.CaesarDecrypt("abcdefghijklmnopqrstuwvxyz0123456789", ciphertext, key))

