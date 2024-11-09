#!/usr/bin/env python3


import sys

def vigenere_encrypt(text, key):
    encrypted_text = []
    key_length = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        encrypted_char = chr(((ord(char) - ord('a')) + (ord(key_char) - ord('a'))) % 26 + ord('a'))
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key_length = len(key)
    for i, char in enumerate(encrypted_text):
        key_char = key[i % key_length]
        decrypted_char = chr(((ord(char) - ord('a')) - (ord(key_char) - ord('a'))) % 26 + ord('a'))
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

# 1 - Test function
print("Hello World!")  

# Encryption
print(vigenere_encrypt("hello", "secretkey"))         
print(vigenere_encrypt("world", "secretkey"))         
print(vigenere_encrypt("encryption", "secretkey"))    
print(vigenere_encrypt("someonecrackedmypassword", "secretkey"))  
print(vigenere_encrypt("poorsecurityhurtseveryone", "secretkey")) 

# Decryption
print(vigenere_decrypt("srnabepakm", "brainstation")) 
print(vigenere_decrypt("ciubrxhrvm", "brainstation"))
print(vigenere_decrypt("cvsbcjtcmqqrt", "brainstation")) 
print(vigenere_decrypt("qfozfwvukqhlilrbfwoekgcaf", "brainstation"))
print(vigenere_decrypt("uyeyhavkuzcjowofwmfplwjrskhmyssywwu", "brainstation"))

# 2 - Command-line input for encrypting/decrypting
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 encryptdecrypt.py <encrypt/decrypt> <text> <key>")
        sys.exit(1)

    direction = sys.argv[1].lower()
    text = sys.argv[2]
    key = sys.argv[3]

    if direction == "encrypt":
        result = vigenere_encrypt(text, key)
    elif direction == "decrypt":
        result = vigenere_decrypt(text, key)
    else:
        print("Invalid direction! Use 'encrypt' or 'decrypt'.")
        sys.exit(1)

    print(f"Result: {result}")



