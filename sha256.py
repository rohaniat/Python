#!/usr/bin/env python3

import hashlib
import sys


def hash_passphrase(passphrase):
    """Hash a passphrase using SHA-256."""
    return hashlib.sha256(passphrase.encode()).hexdigest()

def verify_passphrase(stored_hash, passphrase_given):
    """Verify if the hashed passphrase matches the stored hash."""
    return hash_passphrase(passphrase_given) == stored_hash

# Testing
users = [
    {"name": "DARYL HOWLAND", "passphrase": "husky", "hash": "09e28e9c5875ef3b2b7463e1c9adc3cefbd35af73283f9f9281dc9b8c48f9524"},
    {"name": "MARISSA FERREIRA", "passphrase": "labrador", "hash": "0782cb514029008de13d7e71aa1662c310b08d0d0abb29b3220466c0f3b08c1f"},
    {"name": "TIM SUNG", "passphrase": "beagle", "hash": "6573818d2ffc8a09380b22a5aa517a33cca87f54e51897ee8e64b45166a76e51"},
    {"name": "SIMONE OSTERMANN", "passphrase": "dachshund", "hash": "e05151fd4885688b44dece508de93cfcbe7cacb262d1d3999f9287014ab5bfb7"}
]

print("Hello World!")

# Verification
for user in users:
    name = user["name"]
    passphrase = user["passphrase"]
    stored_hash = user["hash"]
    is_valid = verify_passphrase(stored_hash, passphrase)
    print(f"User: {name}, Passphrase Given: {passphrase}, Valid: {is_valid}")

# Command-line
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 sha256.py <username> <passphrase>")
        sys.exit(1)

    username = sys.argv[1]
    passphrase_given = sys.argv[2]
    
    # Username
    user = next((user for user in users if user["name"].lower() == username.lower()), None)
    
    if user:
        is_valid = verify_passphrase(user["hash"], passphrase_given)
        print(f"User: {username}, Passphrase Given: {passphrase_given}, Valid: {is_valid}")
    else:
        print(f"User: {username} not found")

