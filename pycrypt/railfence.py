# -*- coding: utf-8 -*-

def Encrypt(message, key):
    """Key is the heigth of the rail fence"""
    ciphertext = ""
    for i in range(key):
        ciphertext += message[i]
        counter = key
        while True:
            try:
                ciphertext += message[i+counter]
                counter+=key
            except IndexError:
                break
    return ciphertext