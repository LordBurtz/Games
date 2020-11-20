"""
import hashlib, os

salt = os.urandom(32)

password = input(' Passowrd: ')
key = hashlib.pbkdf2_hmac (
    'sh256',
    password.encode('utf-8'),
    salt,
    100000
)

storage = salt + key
salt_from_storage = storage[:32]
key_from_storage = storage[32:]
"""

import hashlib, os, base64

def hashPasswd(input, salt=os.urandom(32)):
    #salt = os.urandom(32)
    print('salt: ' + str(salt))
    key = hashlib.pbkdf2_hmac (
        'sha256',
        input.encode('utf-8'),
        salt,
        1000000
    )
    print('key' +  str(key))
    store = salt + key
    print(str(store))
    return store

def checkpw():
    with open('passwords', 'rb') as pw:
        content = pw.read()
        salt = content[:32]
        print(salt)
        hashed_pwd = content[32:]
        print(hashed_pwd)
    if str(hashed_pwd) == str(hashPasswd(input(' Input the password: '), salt)):
        print('access')

def main():
    a = hashPasswd(input(' Your password: '))
    with open('passwords', 'wb') as pw:
        pw.write(a)
    print(a)
    checkpw()


if __name__ == '__main__':
    main()
