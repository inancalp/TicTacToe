######## _________________TIC-TAC-TOE_________________ ########

# official code for color yellow = '\033[93m' should be represented as string

color_yellow = '\033[93m'
color_green = '\033[92m'
color_red = '\033[91m'

# original color for CLI: (need to be added at the end of string to keep the balance)

color_white = '\033[0m'

#  ----

underline = '\033[4m'
bold = '\033[1m'

gui = color_green + """
    -------------------------
    | (1,1) | (1,2) | (1,3) |
    -------------------------
    | (2,1) | (2,2) | (2,3) |
    -------------------------
    | (3,1) | (3,2) | (3,3) |
    -------------------------
""" + color_white

possible_inputs = ['1,1', '1,2', '1,3', '2,1', '2,2', '2,3', '3,1', '3,2', '3,3']
s1 = {'1,1', '2,2', '3,3'}
s2 = {'3,1', '2,2', '1,3'}

l1_p1 = []
l2_p1 = []
l3_p1 = []

l1_p2 = []
l2_p2 = []
l3_p2 = []

player1_point = 0
player2_point = 0
playtime_count = 0
x = None
finish = False


# -----------------------------------------||||-------------------------------------------------


def score():
    global x
    global player1_point
    global player2_point
    print('')
    print('----------------------------')
    print(text_bold(text_yellow(' SCOREBOARD:')) + " P1:" + text_red(f'"{str(player1_point)}"') + ", P2:" + text_red(
        f'"{str(player2_point)}"') + color_white)
    print('----------------------------')
    print('')


def renew_gui():
    global gui
    gui = color_green + """
    -------------------------
    | (1,1) | (1,2) | (1,3) |
    -------------------------
    | (2,1) | (2,2) | (2,3) |
    -------------------------
    | (3,1) | (3,2) | (3,3) |
    -------------------------
    """ + color_white


def clear_game_data():
    global playtime_count
    l1_p1.clear()
    l2_p1.clear()
    l3_p1.clear()
    l1_p2.clear()
    l2_p2.clear()
    l3_p2.clear()
    playtime_count = 0


def list_checker_p1():
    def mess1():
        global x
        global player1_point
        global playtime_count
        renew_gui()
        player1_point += 1
        score()
        if player1_point == 3:
            x = True
        else:
            print(gui)
            print(text_yellow("It's (P2)'s TURN"))
            print('')
        clear_game_data()

    if l1_p1.count(l1_p1[-1]) == 3:
        print(text_bold(f' {text_yellow("(P1)")} +1'))
        mess1()
    elif l2_p1.count(l2_p1[-1]) == 3:
        print(text_bold(f' {text_yellow("(P1)")} +1'))
        mess1()
    elif s1.issubset(set(l3_p1)):
        print(text_bold(f' {text_yellow("(P1)")} +1'))
        mess1()
    elif s2.issubset(set(l3_p1)):
        print(text_bold(f' {text_yellow("(P1)")} +1'))
        mess1()


def list_checker_p2():
    def mess2():
        global x
        global player2_point
        global playtime_count
        renew_gui()
        player2_point += 1
        score()
        if player2_point == 3:
            x = True
        else:
            print(gui)
            print(text_yellow("It's P1's TURN"))
            print('')
        clear_game_data()

    if l1_p2.count(l1_p2[-1]) == 3:
        print(text_bold(f' {text_yellow("(P2)")} +1'))
        mess2()
    elif l2_p2.count(l2_p2[-1]) == 3:
        print(text_bold(f' {text_yellow("(P2)")} +1'))
        mess2()
    elif s1.issubset(set(l3_p2)):
        print(text_bold(f' {text_yellow("(P2)")} +1'))
        mess2()
    elif s2.issubset(set(l3_p2)):
        print(text_bold(f' {text_yellow("(P2)")} +1'))
        mess2()


def append_lists_p1(i):
    l1_p1.append(i[0])
    l2_p1.append(i[-1])
    l3_p1.append(i)


def append_lists_p2(i):
    l1_p2.append(i[0])
    l2_p2.append(i[-1])
    l3_p2.append(i)


def finish_function():
    global finish
    finish = True
    print('')
    print(color_yellow + '  Thanks for playing!' + color_white)
    print('')


def text_yellow(text):
    return color_yellow + text + color_white


def text_red(text):
    return color_red + text + color_white


def text_bold(text):
    return bold + text + color_white


def text_white(text):
    return color_white + text + color_white


# -----------------------------------------||||-------------------------------------------------

print('')
print('')
print('     ' + underline + color_red + text_bold('TicTacToe') + color_white)
print('')
print(color_yellow + '  Whoever gets 3 point first will win the game!' + color_white)
print('')

print(color_yellow + '    GL HF!!' + color_white)

print(gui)

# NOTE: data for "x" is stored in the messes of list checker functions for player1 and player2

while x is None:
    while True:
        p1_input = input(text_bold(f'{text_yellow(" (P1)")} Row and Column number: '))
        if p1_input in possible_inputs:
            if p1_input in gui:
                append_lists_p1(p1_input)
                playtime_count += 1
                gui = gui.replace(p1_input, color_yellow + '"X"' + color_green)
                print(gui)
                break
            elif p1_input.lower() == 'quit':
                finish_function()
                break
            else:
                print(text_red('Row,Column ->> TAKEN'))
                continue
        elif p1_input.lower() == 'quit':
            finish_function()
            break
        else:
            print(text_red('Invalid Input'))
            continue
    if finish:
        break
    if playtime_count == 9:
        print(text_bold(' DRAW'))
        clear_game_data()
        renew_gui()
        score()
        print(gui)
        print(text_yellow("It's (P2)'s TURN"))
        print('')
    try:
        list_checker_p1()
    except IndexError:
        pass
    if x:
        print(f" {text_yellow('(P1)')} WON !!!")
        print('')
        break
    while True:
        p2_input = input(text_bold(f'{text_yellow(" (P2)")} Row and Column number: '))
        if p2_input in possible_inputs:
            if p2_input in gui:
                append_lists_p2(p2_input)
                playtime_count += 1
                gui = gui.replace(p2_input, color_yellow + '"O"' + color_green)
                print(gui)
                break
            elif p2_input.lower() == 'quit':
                finish_function()
                break
            else:
                print(text_red('Row,Column ->> TAKEN'))
                continue
        elif p2_input.lower() == 'quit':
            finish_function()
            break
        else:
            print(text_red('Invalid Input'))
            continue
    if finish:
        break
    if playtime_count == 9:
        print(text_bold(' DRAW'))
        clear_game_data()
        renew_gui()
        score()
        print(gui)
        print(text_yellow("It's (P1)'s TURN"))
        print('')
        continue
    try:
        list_checker_p2()
    except IndexError:
        pass
    if x:
        print(f" {text_yellow('(P2)')} WON !!!")
        print('')
        break
