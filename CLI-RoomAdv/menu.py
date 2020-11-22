import time, random, fileinput, sys, hashlib, os
from simple_term_menu import TerminalMenu
from getpass import getpass

def mainMenu():
    main_menu_title = ' Main Menu\n'
    main_menu_items = ['New room', 'Inventar', 'Teleport', 'Customize NOT WORKING PROPERLY !', 'Quit']

    main_menu = TerminalMenu (
        title = main_menu_title,
        menu_entries = main_menu_items,
        menu_cursor = menu_cursor,
        menu_cursor_style = menu_cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )

    main_menu_exit = False

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            newRoom()
        elif main_sel == 1:
            Inventar()
        elif main_sel == 2:
            Teleport()
        elif main_sel == 3:
            Customize()
            main_menu_exit = True
        elif main_sel == 4:
            print('Quitting..')
            sys.exit()

def Customize():
    menu_title = ' Customize here'
    menu_items = ['Cursor', 'Color scheme', 'back']
    menu_back = False

    menu = TerminalMenu(
        title = menu_title,
        menu_entries = menu_items,
        menu_cursor = menu_cursor,
        menu_cursor_style = menu_cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )

    while not menu_back:
        menu_sel = menu.show()
        if menu_sel == 0:
            customizeCursor()
        elif menu_sel == 1:
            colorScheme()
        elif menu_sel == 2:
            menu_back = True
            mainMenu()

def colorScheme():
    menu_title = ' Select a Color Scheme'
    menu_items = ['red', 'blue', 'back']
    menu_back = False

    menu_back = False

    menu = TerminalMenu(
        title = menu_title,
        menu_entries = menu_items,
        menu_cursor = '-> ',
        menu_cursor_style = ('fg_red', 'bold'),
        menu_highlight_style = ('bg_red', 'fg_yellow'),
        cycle_cursor = True,
        clear_screen = True
    )

    global menu_cursor_style
    global menu_style

    while not menu_back:
        menu_sel = menu.show()
        if menu_sel == 0:
            menu_style = ('bg_red', 'fg_yellow')
            menu_cursor_style = ('bg_red', 'bold')
        elif menu_sel == 1:
            menu_style = ('bg_blue', 'fg_gray')
            menu_cursor_style = ('bg_blue', 'bold')
        if menu_sel == 2:
            menu_back = True
            Customize()

def customizeCursor():
    global menu_cursor

    print(' Type the desired cursor below: ')
    new_cursor = input( 'Cursor here: ')
    menu_cursor = str(new_cursor)
    time.sleep(2)

def newRoom():
    randint = random.randint(1, 100)
    if randint < 50:
        Monster()
    elif randint >= 50 and randint < 76:
        Treasure()
    elif randint >= 76:
        Nothing()

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

def main():
    global menu_cursor
    menu_cursor = '-> '
    global menu_cursor_style
    menu_cursor_style = ('fg_red', 'bold')
    global menu_style
    menu_style = ('bg_red', 'fg_yellow')
    global player
    player = ''
    login()
    global weapon
    weapon = 1
    global health
    health = 25

    try:
        with open(str(player + '.inventory')) as inv:
            data = []
            data = inv.read()
    except:
        with open(str(player + '.inventory'), 'a') as inv:
            inv.write('1')
            print('First time? *zwinkersmiley*')
            time.sleep(2)

    mainMenu()

def Monster():
    hp = random.randint(30, 69)

    menu_title = ' Fight for your life\n'
    menu_items = ['attack', 'block', 'retreat', 'quit']
    menu_back = False

    menu = TerminalMenu (
        title = menu_title,
        menu_entries = menu_items,
        menu_cursor = menu_cursor,
        menu_cursor_style = menu_cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )

    monster_dead = False
    debug = True

    while not menu_back:
        global weapon
        global health

        """round based health reduction WIP"""

        if weapon == 1:
            sword = 'a normal sword'
        elif weapon == 2:
            sword = 'Hardened Iron Sword'
        elif weapon == 3:
            sword = 'Ringil'
        elif weapon == 4:
            sword = 'Excalibur'

        menu_sel = menu.show()
        if menu_sel == 0:
            if hp > 0:
                print(' monsterhp: ' + str(hp)   )
                print(' you attacked using ' + sword )
                ap = attack()
                hp = int(hp) - int(ap)
                print(' you attacked dealing ' + str(ap) + ' damage!')
                if hp < 0:
                    print(' monster killed')
                    menu_back = True
                else:
                    print (' ' + str(hp) + ' hp left')
            else:
                print(' you killed the monster, congrats')
                menu_back = True
            time.sleep(4)
        elif menu_sel == 1:
            print(' monsterhp: ' + str(hp)   )
            print(' you blocked')
            print(' ' + str(hp) + ' left')
            time.sleep(3)
        elif menu_sel == 2:
            print(' fly you fools!')
            time.sleep(3)
            menu_back = True
            mainMenu()
        elif menu_sel == 3 and debug == True:
            sys.exit()

def Treasure():
    menu_title = ' You found a treasure!\n Yey'
    menu_items = ['open the chest', 'go further', 'back']
    menu_back = False

    menu = TerminalMenu (
        title = menu_title,
        menu_entries = menu_items,
        menu_cursor = menu_cursor,
        menu_cursor_style = menu_cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )

    while not menu_back:
        '!!write the > first then =!!'
        rabbit_hole = ' Going deeper into the rabbit hole'
        menu_sel = menu.show()
        if menu_sel == 0:
            chance = random.randint(1, 100)
            if chance <= 50 and chance > 15:
                print(' You found a Normal Sword')
                with open('inventory', 'a') as inv:
                    inv.write('1')
                time.sleep(1.5)
                print(rabbit_hole)
                time.sleep(2)
                newRoom()
            elif chance > 50 and chance < 76:
                print(' You found a Hardened Iron Sword')
                with open('inventory', 'a') as inv:
                    inv.write('2')
                time.sleep(1.5)
                print(rabbit_hole)
                time.sleep(2)
                newRoom()
            elif chance >= 76 and chance <= 88:
                print(' You found Ringil\n Congrats!')
                with open('inventory', 'a') as inv:
                    inv.write('3')
                time.sleep(1.5)
                print(rabbit_hole)
                time.sleep(2)
                newRoom()
            elif chance > 88 and chance < 94:
                print(' You found Excalibur!\n Congrats!')
                with open('inventory', 'a') as inv:
                    inv.write('4')
                time.sleep(1.5)
                print(rabbit_hole)
                time.sleep(2)
                newRoom()
            elif chance <= 15 or chance >= 94:
                print(' You unlucky bastard..\n this chest is empty... ._.')
                print(rabbit_hole)
                time.sleep(3.3)
                newRoom()

        elif menu_sel == 1:
            newRoom()

        elif menu_sel == 2:
            menu_back = True

def Nothing():
    print(' this room is empty\n nothing to see here\n yey!')
    time.sleep(2)

def Inventar():
    menu_title = ' Your inventory: ._.'
    menu_items = ['list the available ones', 'choose', 'back']
    menu_back = False

    menu = TerminalMenu (
        title = menu_title,
        menu_entries = menu_items,
        menu_cursor = menu_cursor,
        menu_cursor_style = menu_cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )
    menu_exit = False

    while not menu_exit:
        main_sel = menu.show()

        if main_sel == 0:
            with open('inventory') as inv:
                inven = []
                inven = inv.read()
            items = set()
            for item in inven:
                if item == '1':
                    items.add('Normal sword')
                elif item == '2':
                    items.add('Hardened Iron sword')
                elif item == '3':
                    items.add('Ringil')
                elif item == '4':
                    items.add('Excalibur')
            print(items)
            time.sleep(2)

        if main_sel == 1:
            choose()

        if main_sel == 2:
            print('going back')
            menu_exit = True

def choose():
     """!!!this is fucking wrong intendet!!!"""
     menu_title = ' Choose what you want to choose'
     menu_items = ['weapons', 'armor', 'back']
     menu_back = False

     menu = TerminalMenu (
         title = menu_title,
         menu_entries = menu_items,
         menu_cursor = menu_cursor,
         menu_cursor_style = menu_cursor_style,
         menu_highlight_style = menu_style,
         cycle_cursor = True,
         clear_screen = True
     )

     while not menu_back:
         menu_sel = menu.show()
         if menu_sel == 0:
             chooseWeapon()
         elif menu_sel == 1:
             chooseArmor()
         elif menu_sel == 2:
             print('going back')
             menu_back = True

def chooseWeapon():
    menu_title = ' Choose your weapon here'
    menu_items = ['Normal Sword', 'Hardened Iron Sword', 'Ringil', 'Excalibur', 'back']
    menu_back = False

    menu = TerminalMenu (
        title = menu_title,
        menu_entries = menu_items,
        menu_cursor = menu_cursor,
        menu_cursor_style = menu_cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )

    while not menu_back:
        noot = 'you dont have this weapon'
        menu_sel = menu.show()
        if menu_sel == 0:
            with open('inventory') as inv:
                inven = inv.read()
            if '1' in inven:
                print('success')
                global weapon
                weapon = 1
                time.sleep(1)
            else:
                print(noot)
                time.sleep(1)

        elif menu_sel == 1:
            with open('inventory') as inv:
                inven = inv.read()
            if '2' in inven:
                weapon= 2
                print('success')
                time.sleep(2)
            else:
                print(noot)
                time.sleep(1)


        elif menu_sel == 2:
            with open('inventory') as inv:
                inven = inv.read()
            if '3' in inven:
                weapon = 3
                print('success')
                time.sleep(1)
            else:
                print(noot)
                time.sleep(1)

        elif menu_sel == 3:
            with open('inventory') as inv:
                inven = inv.read()
            if '4' in inven:
                weapon = 4
                print('success')
                time.sleep(1)
            else:
                print(' you dont have this weapon')
                time.sleep(1)

        elif menu_sel == 4:
            menu_back = True

def attack():
    global weapon
    if weapon == 1:
        return random.randint(3, 9)
    elif weapon == 2:
        return random.randint(7, 15)
    elif weapon == 3:
        return random.randint(10, 17)
    elif weapon == 4:
        return random.randint(15, 25)

def Teleport():
    print('Telepport comming soon, too')
    time.sleep(2)

def login():
    global player
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
                player = new_username

        elif str(username) in players:
            with open(username + '.password', 'rb') as user_password:
                content = user_password.read()
                salt = content[:32]
                hashed_pwd = content

                if str(hashed_pwd) == str(hashPasswd(getpass(' Password: '), salt)):
                    print('access')
                    player = username
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

if __name__ == '__main__':
    main()
