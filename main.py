import hashlib

string = "harsh"
result = hashlib.md5(string.encode())

print("The hexadecimal equivalent of hash is: ", result.hexdigest())
