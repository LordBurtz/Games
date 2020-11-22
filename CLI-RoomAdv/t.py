#testing
import hashlib, os
from getpass import getpass




os.path.isfile("/etc/password.txt")
True




def init_process():
    try:

        with open('players', 'r') as pl:
            players = []
            players = pl.readlines()

        print(players)
        username = input(' Username: ')

        if str(username) == 'new':
            print(' Creating one..')
            new_username = input(' Username: ')
            new_password = getpass(' Password: ')
            new_hash = hashPasswd(new_password)

            with open(new_username + '.password', 'wb') as new:
                new.write(new_hash)

            with open('players', 'a') as p:
                p. writelines('\n' + new_username)

        elif str(username) in players:
            with open(username + '.password', 'rb') as user_password:
                content = user_password.read()
                salt = content[:32]
                hashed_pwd = content

                if str(hashed_pwd) == str(hashPasswd(getpass(' Password: '), salt)):
                    print('access')
                else:
                    print('failed')

        else:
            print(' This user does not exit...')
            print(' Creating one..')
            new_username = input(' Username: ')
            new_password = getpass(' Password: ')
            new_hash = hashPasswd(new_password)

            with open(new_username + '.password', 'wb') as new:
                new.write(new_hash)

            with open('players', 'a') as p:
                p. writelines('\n' + new_username)

    except:
        print(' Creating one..')
        new_username = input(' Username: ')
        new_password = getpass(' Password: ')
        new_hash = hashPasswd(new_password)

        with open(new_username + '.password', 'wb') as new:
            new.write(new_hash)

        with open('players', 'a') as p:
            p. writelines('\n' + new_username)




def hashPasswd(input, salt=os.urandom(32)):
    #salt = os.urandom(32)
    #print('salt: ' + str(salt))
    key = hashlib.pbkdf2_hmac (
    'sha256',
    input.encode('utf-8'),
    salt,
    1000000
    )
    #print('key' +  str(key))
    store = salt + key
    #print('store this' + str(store))
    return store

if __name__ == '__main__':
    init_process()
