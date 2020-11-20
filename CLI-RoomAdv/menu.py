import time, random, fileinput, sys
from simple_term_menu import TerminalMenu
import roomtest as rt
import monsterfight as mf

def main():
    global menu_cursor
    menu_cursor = '-> '
    global menu_cursor_style
    menu_cursor_style = ('fg_red', 'bold')
    global menu_style
    menu_style = ('bg_red', 'fg_yellow')
    global weapon
    global start
    start = False
    mainMenu()

def mainMenu():
    main_menu_title = ' Main Menu\n'
    main_menu_items = ['New room', 'Inventar', 'Teleport', 'Quit']

    if start == False:
        weapon = 1
        start = True
    main_menu_exit = False


    main_menu = TerminalMenu (
        title = main_menu_title,
        menu_entries = main_menu_items,
        menu_cursor = menu_cursor,
        menu_cursor_style = menu_cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            randint = random.randint(1, 100)
            if randint < 50:
                Monster()
            elif randint >= 50 and randint < 76:
                Treasure()
            elif randint >= 76:
                Nothing()
        elif main_sel == 1:
            Inventar()
        elif main_sel == 2:
            Teleport()
        elif main_self == 3:
            main_menu_exit = True
            print('Quitting..')


def Monster():
    hp = random.randint(30, 69)

    menu_title = ' Fight for your life\n'
    menu_items = ['attack', 'block', 'retreat', 'quit']
    global menu_cursor
    menu_cursor = '-> '
    global menu_cursor_style
    menu_cursor_style = ('fg_red', 'bold')
    global menu_style
    menu_style = ('bg_red', 'fg_yellow')
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
        menu_sel = menu.show()
        print(' monsterhp: ' + str(hp)   )
        if menu_sel == 0:
            if hp > 0:
                print(' you attacked with a stone sword')
                ap = attack()
                hp = int(hp) - int(ap)
                print(ap)
                if hp < 0:
                    print(' monster killed')
                    menu_back = True
                else:
                    print (' ' + str(hp) + ' hp left')
            else:
                print(' you killed the monster, congrats')
                menu_back = True
            time.sleep(2)
        elif menu_sel == 1:
            print(' you blocked')
            print(' ' + str(hp) + ' left')
            time.sleep(2)
        elif menu_sel == 2:
            print(' falling back')
            time.sleep(2)
            menu_back = True
        elif menu_sel == 3 and debug == True:
            sys.exit()

def Treasure():
    menu_title = ' Entered new room\n'
    menu_items = ['attack', 'block', 'back']
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

    print('Treasure yey !')
    time.sleep(2)

def Nothing():
    print(' nothing to see here\n yey!')
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
                    items.add('Stone sword')
                elif item == '2':
                    items.add('Iron sword')
                elif item == '3':
                    items.add('shield')
            print(items)
            time.sleep(2)

        if main_sel == 1:
            choose()

        if main_sel == 2:
            print('going back')
            time.sleep(2)
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
             time.sleep(1)
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
                weapon = 1
                time.sleep(2)
            else:
                print(noot)
                time.sleep(1)

        elif menu_sel == 1:
            with open('inventory') as inv:
                inven = inv.read()
            if '2' in inven:
                weapon = 2
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
                time.sleep(2)
            else:
                print(noot)
                time.sleep(1)

        elif menu_sel == 3:
            with open('inventory') as inv:
                inven = inv.read()
            if '4' in inven:
                weapon = 4
                print('success')
                time.sleep(2)
            else:
                print('you dont have this weapon')
                time.sleep(1)

        elif menu_sel == 4:
            time.sleep(1)
            menu_back = True

def attack():
    if weapon == 1:
        return random.randint(3, 9)
    elif weapon == 2:
        return random.randint(7, 13)
    elif weapon == 3:
        return random.randint(10, 17)
    elif weapon == 4:
        return random.randint(15, 25)

def Teleport():
    print('Telepport comming soon, too')
    time.sleep(2)

if __name__ == '__main__':
    main()
