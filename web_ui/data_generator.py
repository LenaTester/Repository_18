import random
import string
import secrets

def random_string(length=5):
    return ''.join((random.choice(string.ascii_letters) for _ in range(length)))

def random_phone(length=10):
    return ''.join((random.choice(string.digits) for _ in range(length)))

def random_password(length=8):
    abc = string.ascii_letters
    digits = string.digits
    return "".join(secrets.choice(digits + abc) for _ in range(length))

def random_zip(length=5):
    return ''.join((random.choice(string.digits) for _ in range(length)))

