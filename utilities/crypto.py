#!/usr/bin/python3
from cryptography.fernet import Fernet

def encrypted(pswd):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        pswd_bytes = pswd.encode()
        ciphered_pswd = cipher_suite.encrypt(pswd_bytes)
        return [ciphered_pswd, key]

def denrcypted(pswd, key):
    cipher_suite = Fernet(key)
    password = cipher_suite.decrypt(pswd)
    return password.decode()