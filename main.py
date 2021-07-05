import hashlib


def str2md5(string_p):
    result = hashlib.md5(string_p.encode())
    return result.hexdigest()


string_v = input('Enter the string you want to encrypt: ')
print(f'The MD5 encyption of {string_v} is {str2md5(string_v)}')
