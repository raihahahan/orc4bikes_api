import hashlib

hashed = hashlib.sha256("".encode()).hexdigest()
print(hashed)