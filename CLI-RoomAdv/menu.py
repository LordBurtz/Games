import time, random, fileinput, sys, hashlib, os, shutil
from simple_term_menu import TerminalMenu
from getpass import getpass

def mainMenu():
    main_menu_title = ' Main Menu\n'
    main_menu_items = ['New room', 'Inventar', 'Teleport', 'Customize NOT WORKING PROPERLY !', 'Quit', ' ', 'Admin']

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

    #with open(str(player + '.purse'))

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
        elif main_sel == 6:
            admin()

def admin():
    print(' Admin panel: ')
    adminLog = getpass(' Input admin password: ')

    i = 1
    while i < 4:
        if str(adminLog) == str('admin'):
            kurt()
            break
        elif i >= 3:
            print(' too many wrong passwords entered.. ')
            break
        else:
            print('\n failed\n wrong password entered\n')
            print(' ' + str(3 - i) + ' tries left')
            i += 1

def kurt():
    global menu_cursor
    global menu_cursor_style
    global menu_style

    menu_title = ' Holy Admin panel'
    menu_items = [' delete user', 'change user password', 'reset user', 'self destruct', 'back']
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
            print(' Whom to delete?')
            deleted_user = input(' Username: ')
            check = input(' Sure? Y/n ')
            print(' deleting ' + deleted_user)
            if check == 'Y':
                try: shutil.rmtree(str('RoomAdvGame/' + deleted_user))
                except: print('fuf')

                with open('RoomAdvGame/players', 'r') as rpl:
                    content = []
                    content = rpl.readlines()
                if deleted_user in content:
                    content.remove(deleted_user)
                    with open('RoomAdvGame/players', 'w') as rpl:
                        i = 0
                        for item in content:
                            rpl.write(content[i])
                            i += 1
                else:
                    print(' user does not exist')

        elif menu_sel == 1:
            print(' Whose password to change?')
            change_user = input(' User: ')
            with open('RoomAdvGame/players', 'r') as rpl:
                content = []
                content = rpl.readlines()
            if change_user in content:
                new_password = getpass(' New password: ')
                with open('RoomAdvGame/' + change_user + '/' + change_user + '.password', 'wb') as pwd:
                    pwd.write(hashPasswd(new_password))
                    print(' password updated')
                    time.sleep(1)
            else:
                print(' this user does not exist')
                time.sleep(2)

        elif menu_sel == 2:
            print(' Who to reset?')
            reset_user = input(' user: ')
            with open('RoomAdvGame/players', 'r') as rpl:
                content = []
                content = rpl.readlines()
            if reset_user in content:
                print(' Sure to reset ' + reset_user + '?')
                choice = input(' Sure? Y/n ')
                if choice == Y:
                    with open('RoomAdvGame/' + reset_user + '/' + reset_user + '.inventory', 'w') as i:
                        i.write('1')
                    with open('RoomAdvGame/' + reset_user + '/' + reset_user + '.purse', 'w') as i:
                        i.write('50')
                    print(' successfull resetted')
                    time.sleep(1)
                else:
                    print(' ok have a great day')

        elif menu_sel == 3:
            print(' Do you really want to self destruct?')
            choice = input(' Y/n --> ')
            if choice == 'Y':
                shutil.rmtree('RoomAdvGame')
                os.remove(sys.argv[0])
                print(' bravo six going dark')
                print(' cya')
                time.sleep(2.5)
                sys.exit()
            else:
                print(' Buhr?')
                time.sleep(1)
        elif menu_sel == 4:
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
    os.system('clear')
    print('\n RoomAdvGame presented by Fingolfin')
    time.sleep(2)
    os.system('clear')
    global menu_cursor
    menu_cursor = '-> '
    global menu_cursor_style
    menu_cursor_style = ('fg_red', 'bold')
    global menu_style
    menu_style = ('bg_red', 'fg_yellow')
    global player
    global motype
    global weapon
    weapon = 1
    global health
    health = 42 + 17

    login()
    test()
    mainMenu()

def test():
    global player
    try:
        with open(str('RoomAdvGame/' + player + '/' + player + '.inventory'), 'r') as inv:
            data = []
            data = inv.read()
    except:
        with open(str('RoomAdvGame/' +  player + '/' + player + '.inventory'), 'a') as inv:
            inv.write('1')
            print('First time? *zwinkersmiley*')
            time.sleep(2)

    global inventory
    inventory = str(player + '.inventory')
    global coins

    try:
        with open(str('RoomAdvGame/' + player + '/' + player + '.purse'), 'r') as pu:
            coins = pu.read()
    except:
        with open(str('RoomAdvGame/' + player + '/' + player + '.purse'), 'w') as pu:
            pu.write(str(50))

def add2purse():
    global player
    global coins
    with open(str('RoomAdvGame/' + player + '.purse'), 'w') as pu:
        swap = int(pu.read())
        swap = int(swap) + int(coins)
        pu.write(int(swap))
        coins = 0

def Monster():
    global motype

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

    if hp < 40:
        motype = 1
    elif hp >= 40 and hp < 50:
        motype = 2
    elif hp >= 50 and hp < 60:
        motype = 3
    elif hp >= 60 and hp < 70:
        motype = 4

    monster_dead = False
    debug = True

    while not menu_back:
        global weapon
        global health
        global coins

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
                print(' you attacked using ' + sword )
                ap = attack()
                hp = int(hp) - int(ap)
                moap = monsterattack()
                health = health - moap

                print(' you attacked dealing ' + str(ap) + ' damage!')
                print(' The monster has ' + str(hp) + ' hp left')
                print(' The monster attacked dealing ' + str(moap) + ' hp damage')
                print(' you have ' + str(health) + ' hp left')

                if hp <= 0:
                    print(' monster killed')
                    reward = reward()
                    print(' you got ' + str(reward) + ' coins')
                    menu_back = True
                    mainMenu()

                elif health <= 0:
                    print(' You are dead you miserable looser')
                    coins = 0

            else:
                print(' you killed the monster, congrats')
                menu_back = True
            time.sleep(6)
        elif menu_sel == 1:
            moap = monsterattack()
            health = health - int(moap)* 0.42

            print(' The monster has ' + str(hp) + ' hp left'  )
            print(' you blocked')
            print(' the monster attacked and dealt ' + str(moap) + ' damage' )
            print(' you have ' + str(health) + ' hp left')
            time.sleep(6)
        elif menu_sel == 2:
            print(' fly you fools!')
            time.sleep(3)
            menu_back = True
            mainMenu()
        elif menu_sel == 3 and debug == True:
            sys.exit()

def monsterattack():
    global motype

    if motype == 1:
        return (random.randint(2, 5))
    elif motype == 2:
        return (random.randint(4, 7))
    elif motype == 3:
        return (random.randint(6, 10))
    elif motype == 4:
        return (random.randint(8, 13))
    else:
        print('unknown monstertype what happened lol??')
        sys.exit()

def reward():
    global motype

    if motype == 1:
        reward = (random.randint(10, 20))
    elif motype == 2:
        reward = (random.randint(21, 35))
    elif motype == 3:
        reward = (random.randint(36, 57))
    elif motype == 4:
        reward =  (random.randint(58, 83))
    else:
        print(' unknown monstertype what happened lol?')
        sys.exit()

    with open(str('RoomAdvGame/' + player + '.purse'), 'w') as inv:
        coins_atm = inv.read()
        coins2write = int(coins_atm + reward)
        inv.write(coins2write)

    return reward

def Treasure():
    menu_title = ' You found a treasure!\n Yey'
    menu_items = ['open the chest', 'go further', 'back']
    menu_back = False
    global palyer
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
                with open('RoomAdvGame/' + player + '/' + inventory, 'a') as inv:
                    inv.write('1')
                time.sleep(1.5)
                print(rabbit_hole)
                time.sleep(2)
                newRoom()
            elif chance > 50 and chance < 76:
                print(' You found a Hardened Iron Sword')
                with open('RoomAdvGame/' + player + '/' + inventory, 'a') as inv:
                    inv.write('2')
                time.sleep(1.5)
                print(rabbit_hole)
                time.sleep(2)
                newRoom()
            elif chance >= 76 and chance <= 88:
                print(' You found Ringil\n Congrats!')
                with open('RoomAdvGame/' + player + '/' + inventory, 'a') as inv:
                    inv.write('3')
                time.sleep(1.5)
                print(rabbit_hole)
                time.sleep(2)
                newRoom()
            elif chance > 88 and chance < 94:
                print(' You found Excalibur!\n Congrats!')
                with open('RoomAdvGame/' + player + '/' + inventory, 'a') as inv:
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
    global player
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
            with open('RoomAdvGame/' + player + '/' + inventory) as inv:
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
    global player
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
            with open('RoomAdvGame/' + player + '/' + inventory) as inv:
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
            with open('RoomAdvGame/' + player + '/' + inventory) as inv:
                inven = inv.read()
            if '2' in inven:
                weapon= 2
                print('success')
                time.sleep(2)
            else:
                print(noot)
                time.sleep(1)


        elif menu_sel == 2:
            with open('RoomAdvGame/' + player + '/' + inventory) as inv:
                inven = inv.read()
            if '3' in inven:
                weapon = 3
                print('success')
                time.sleep(1)
            else:
                print(noot)
                time.sleep(1)

        elif menu_sel == 3:
            with open('RoomAdvGame/' + player + '/' + inventory) as inv:
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

    if os.path.isfile('RoomAdvGame/players'):
        print('test') #implementing subdirs!!
        with open('RoomAdvGame/players', 'r') as pl:
            players = []
            players = pl.readlines()
        print(' Type "new" for a new player')
        print(' Idiots: --> ' + str(players))
        username = input(' Username: ')


                    #
        if str(username + '\n') in players or str(username) in players:
            with open('RoomAdvGame/' + username + '/' + username + '.password', 'rb') as user_password:
                content = user_password.read()
                salt = content[:32]
                hashed_pwd = content
            i = 1
            print('break #1')
            time.sleep(2)
            while i < 4:
                if str(hashed_pwd) == str(hashPasswd(getpass(' Password: '), salt)):
                    print(' accessed')
                    player = username
                    break
                elif i >= 3:
                    print(' too many wrong passwords entered.. \n exiting')
                    sys.exit()
                else:
                    print('\n failed\n wrong password entered\n')
                    print(' ' + str(3 - i) + ' tries left')
                    i += 1


        elif str(username) == 'new':
            print(' Creating one..')
            new_username = input(' Username: ')
            new_password = getpass(' Password: ')
            new_hash = hashPasswd(new_password)

            os.mkdir('RoomAdvGame/' + new_username)

            with open('RoomAdvGame/' + new_username + '/' + new_username + '.password', 'wb') as new:
                new.write(new_hash)

                with open('RoomAdvGame/players', 'a') as p:
                    p. writelines('\n' + new_username)
                    player = new_username

        else:
            print(' This user does not exit...')
            newUser()

    else:
        print(' First Startup?')
        newUser()

def newUser():
    global player

    print(' Creating new user..')
    new_username = input(' Username: ')
    new_password = getpass(' Password: ')
    new_hash = hashPasswd(new_password)

    if not os.path.exists('RoomAdvGame'):
        os.mkdir('RoomAdvGame')

    os.mkdir('RoomAdvGame/' + new_username)

    with open('RoomAdvGame/' + new_username + '/' + new_username + '.password', 'wb') as new:
        new.write(new_hash)

    with open('RoomAdvGame/players', 'a') as p:
        p.writelines('\n' + new_username)
        player = new_username

if __name__ == '__main__':
    main()
