#!/bin/python3

from single_byte_xor_cipher import decrypt

def find_xorred(words):
    decrypt(words[0])    

if __name__ == '__main__':
    words = []
    with open('4.txt', 'r') as f:
        for line in f:
            words.append(bytes.fromhex(line.strip()))
    # print(*words[:10], sep='\n')
    xorred = find_xorred(words)
    print(xorred)
