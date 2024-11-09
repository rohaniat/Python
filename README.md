# Python Encryption & Decryption Tool

This repository provides a Python-based encryption and decryption tool utilizing a Vigenère Cipher. Additionally, it includes a SHA-256 hashing feature to verify passphrases for user authentication.

## Files in this Repository

- **encryptdecrypt.py**: Python script containing functions for text encryption, decryption, command-line input handling, and passphrase hashing and verification.
- **sha256.py**: Script for SHA-256 hashing.

## Project Overview
Create a Python Encryption & Decryption Tool
In this deliverable you will utilize Python to create a Simple Text Encryption and Decryption Tool.

Set Up Your Environment
Create a new Python file. Remember to use the file extension .py and don't include any spaces in your filename!

At the top of your file, add the following: #!/usr/bin/env python3

Add a line to your file that will print Hello World!

When you're ready to run your file, you'll do so by typing the following into your console: python3 name_of_file.py

Test it out to ensure that your file is executing properly.

Part 1
Write functions to encrypt and decrypt text using a Vignere Cipher, given a single word as a secret key. Your function will only accept letters, and you can assume the letters will always be lowercase. No spaces will be included in the message or the cipher key.

For example, if the message was welcometobrainstation and the secret key was cybersecurity, the encrypted text would be ycmgfeivisztgpquekasp. As well, if the encrypted text was ycmgfeivisztgpquekasp and the secret key was cybersecurity, the decrypted text would be welcometobrainstation

Encrypt the following text with the key: secretkey
"hello"
"world"
"encryption"
"someonecrackedmypassword"
"poorsecurityhurtseveryone"
Decrypt the following encrypted text with the key brainstation
"srnabepakm"
"ciubrxhrvm"
"cvsbcjtcmqqrt"
"qfozfwvukqhlilrbfwoekgcaf"
"uyeyhavkuzcjowofwmfplwjrskhmyssywwu"
Part 2
Modify your program to receive input from the user using the command line. You should receive the following:

direction as to whether you are encrypting or decrypting
text to encrypt/decrypt
secret key to shift your message
Part 3
A company is in the midst of a security overhaul. Before all their new security policies have been instigated, they've implemented a "passphrase for authentication" system where when a user is in need of assistance, they must give you their passphrase. You must check that the passphrase given is the same as the passphrase that is stored. You have a list of these passphrases on hand, but all the passphrases are hashed to ensure security and privacy.

Using the hashlib library, create a function that will hash a passphrase using the SHA-256 hashing algorithm.

Using the following information, determine whether the following users are who they say they are:
NAME OF USER	PASSPHRASE GIVEN	HASH STORED
DARYL HOWLAND	husky	09e28e9c5875ef3b2b7463e1c9adc3cefbd35af73283f9f9281dc9b8c48f9524
MARISSA FERREIRA	labrador	0782cb514029008de13d7e71aa1662c310b08d0d0abb29b3220466c0f3b08c1f
TIM SUNG	beagle	6573818d2ffc8a09380b22a5aa517a33cca87f54e51897ee8e64b45166a76e51
SIMONE OSTERMANN	dachshund	e05151fd4885688b44dece508de93cfcbe7cacb262d1d3999f9287014ab5bfb7

Write a function that will check the hashed passphrase to the hash stored and return to you a boolean value representing whether the user has given the proper passphrase or not.

