import time
from delay import delay_print # needs to be recreated and implemented due to file coruption
# this essentailly took each out put to the terminal and printed letters one by one at a set speed.
from reboot_delay import screen_roll
import countdown # needs to be recreated and implemented due to file coruption
# This was a countdown function that would countdown from 10 and end the program once it reached 0


def unknown():
    print('--------------------------------------------------------------- \n')

    clue = ("I am a creature of the mind, \n"
            "I exist only in thought. \n"
            "I can be powerful or weak, \n"
            "It all depends on the beholder. \n"
            "\n"
            "I am not a spell, nor am I a magic item. \n"
            "I am something much more abstract. \n"
            "I am a concept, \n"
            "And my name is \n")
    delay_print(clue)

    opt = input('> \n')
    if opt.lower() == 'fear':
        delay_print('HEr0s LiIve - Rerys Werj')
        menu()
    else:
        clue = ' ...... \n'
        delay_print('System powering down.')


def system():
    print('--------------------------------------------------------------- \n')
    system_menu = ('1: Power \n'
                   '2: Engine \n'
                   '3: Drill \n'
                   '4: MA1_n \n')
    delay_print(system_menu)

    try:
        opt = input('> \n')

        if opt.isdigit():
            raise TypeError

        if opt.lower() == 'power':
            delay_print('Power gem drained. Recharge to start engine \n')
            system()
        elif opt.lower() == 'engine':
            delay_print('Engine damaged, suggest to power down and maintenance before moving. \n')
            system()
        elif opt.lower() == 'drill':
            delay_print('Drill fully operational \n')
            system()
        elif opt.lower() == 'main':
            back = input('Back to main? Y/N \n')
            delay_print(back)
            if back.lower() == 'y':
                menu()
            elif back.lower() == 'n':
                settings()
        else:
            system()
    except TypeError:
        delay_print("Num3r1c fa1lur3......\n")
        time.sleep(0.5)
        system()


def settings():
    print('--------------------------------------------------------------- \n')
    setting_menu = ('1: Self Destruct \n'
                    '2: System Reboot \n'
                    '3: Return to command \n'
                    '4: Power down \n'
                    '5: MA1_n \n')
    delay_print(setting_menu)

    try:
        opt = input('> \n')

        if opt.isdigit():
            raise TypeError

        if opt.lower() == 'self destruct':
            delay_print('Do you wish to initiate self destruct? Y/N \n')
            user = input('> \n')
            if user.lower() == 'y':
                countdown.countdown()
            elif user.lower() == 'n':
                delay_print('Back to settings \n')
                settings()
            else:
                settings()
        elif opt.lower() == 'system reboot':
            delay_print('Do you wish to reboot? Y/N \n')
            user = input('> \n')
            if user.lower() == 'y':
                start()
            elif user.lower() == 'n':
                delay_print('Back to settings \n')
                settings()
            else:
                settings()
        elif opt.lower() == 'return to command':
            delay_print('Do you wish to return to command? Y/N \n')
            user = input('> \n')
            if user.lower() == 'y':
                delay_print('Error!!!! \n'
                            'Engine damaged \n')
                countdown.countdown()
            elif user.lower() == 'n':
                delay_print('Back to settings \n')
                settings()
            else:
                settings()
        elif opt.lower() == 'power down':
            delay_print('Do you wish to power down? Y/N \n')
            user = input('> \n')
            if user.lower() == 'y':
                delay_print('Powering down')
            elif user.lower() == 'n':
                delay_print('Back to settings \n')
                settings()
            else:
                settings()
        elif opt.lower() == 'main':
            back = input('Back to main? Y/N \n')
            delay_print(back)
            if back.lower() == 'y':
                menu()
            elif back.lower() == 'n':
                settings()
            else:
                settings()
        else:
            settings()
    except TypeError:
        print("Num3r1c fa1lur3......\n")
        time.sleep(0.5)
        settings()


def logs():
    print('--------------------------------------------------------------- \n')
    log_menu = ('1: Cr3w \n'
                '2: Day of EmbARkm3nt \n'
                '3: M1ssi_on \n'
                '4: Inc1_d3nts \n'
                '5: New Orders \n'
                '6: MA1_n \n')
    delay_print(log_menu)

    try:
        opt = int(input('> \n'))

        if opt == 1:
            crew = '10 Animated Armours \n'
            delay_print(crew)
            logs()
        elif opt == 2:
            DoE = '1980--(late) \n'
            delay_print(DoE)
            logs()
        elif opt == 3:
            mission = 'Attack Nas na Riogh \n'
            delay_print(mission)
            logs()
        elif opt == 4:
            incident1 = 'Magiteck timer malfunction \n'
            incident2 = 'earthquake forced direction change \n'
            incident3 = 'WARNING INTRUDER!!!! \n'
            incident4 = 'Resume Mission with updated crew \n'
            delay_print(incident1)
            delay_print(incident2)
            delay_print(incident3)
            delay_print(incident4)
            logs()
        elif opt == 5:
            orders = ('Vessel under command from new commander as of 2 months \n'
                      'Follow previous mission but with and update to crew\n '
                      'Kill all who help the tyrant! \n')
            delay_print(orders)
            logs()
        elif opt == 6:
            back = input('Back to main? Y/N \n')
            delay_print(back)
            if back.lower() == 'y':
                menu()
            elif back.lower() == 'n':
                logs()
        else:
            logs()
    except ValueError:
        print("AlPhachAract3r fa1lur3......\n")
        time.sleep(0.5)
        logs()


def menu():
    print('--------------------------------------------------------------- \n')
    inner_menu = ('Ma1_n \n'
                  '1: L0gs \n'
                  '2: Sy*$3em \n'
                  '3: S3tt1ng5 \n'
                  '4: s%4@2*&-90 \n')
    delay_print(inner_menu)

    try:
        opt = int(input('> \n'))

        if opt == 1:
            logs()
        elif opt == 2:
            system()
        elif opt == 3:
            settings()
        elif opt == 4:
            unknown()
        else:
            menu()
    except ValueError:
        print("AlPhachAract3r fa1lur3......\n")
        time.sleep(0.5)
        menu()


def login_riddles():
    print('--------------------------------------------------------------- \n')
    delay_print('5 times you will be asked, guess enough correct to pass. \n'
                'If you fail be prepared to bbbbaaaa......... \n'
                '\n')
    count = 0

    riddle1 = ('What always runs but never walks, \n'
               'Often murmurs, never talks, \n'
               'Has a bed but never sleeps, \n'
               'An open mouth that never eats? \n')

    delay_print(riddle1)
    user_input = input('> \n')
    if user_input.lower() == 'a river':
        count += 1
        print('Correct \n')
    else:
        print('Incorrect \n')

    riddle2 = ('My life can be measured in hours, \n'
               'I only serve to be devoured, \n'
               'Slim, I am quick, \n'
               'Fat, I am slow, \n'
               'Wind is my foe \n')

    delay_print(riddle2)
    user_input = input('> \n')
    if user_input.lower() == 'a candle':
        count += 1
        print('Correct \n')
    else:
        print('Incorrect \n')

    riddle3 = ('If you drop me, I’m sure to crack, \n'
               'Give me a smile, and I’ll always smile back, \n')

    delay_print(riddle3)
    user_input = input('> \n')
    if user_input.lower() == 'a mirror':
        count += 1
        print('Correct \n')
    else:
        print('Incorrect \n')

    riddle4 = ('What has cities, but no houses, \n'
               'forests, but no trees, \n'
               'and water, but no fish? \n')

    delay_print(riddle4)
    user_input = input('> \n')
    if user_input.lower() == 'a map':
        count += 1
        print('Correct \n')
    else:
        print('Incorrect \n')

    riddle5 = ('My challenge has made men throughout time stumble, \n'
               'I have defeated kings and left wise men humble, \n'
               'You see me now, but I am most often heard, \n'
               'and have killed men when with bullets paired, \n'
               'You might break a sweat when fighting with me, \n'
               'but I"ll exert no pressure on your body, \n'
               'with a direct approach you can never find victory, \n'
               'work laterally rather than literally. \n'
               'What am I? \n')
    delay_print(riddle5)
    user_input = input('> \n')
    if user_input.lower() == 'a riddle':
        count += 1
        print('Correct \n')
    else:
        print('Incorrect \n')

    if count < 2:
        print('Access denied \n')
        countdown.countdown()
    else:
        menu()


def start():
    print('press /')
    inpt = input('> \n')
    error_msg = 'Error! Engine overloading \n'
    malfunc_msg = 'Magiteck malfunction \n'
    files_msg = 'Some systems and files have been lost or damaged \n'
    reboot_msg = 'Do you wish to reboot? \n'
    if inpt == '/':
        delay_print(error_msg)
        delay_print(malfunc_msg)
        delay_print(files_msg)
        delay_print(reboot_msg)

        inpt = input("> Y/N?")
        if inpt.lower() == 'y':
            screen_roll()
            login_riddles()
        elif inpt.lower() == 'n':
            start()
    else:
        start()


start()
