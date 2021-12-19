######## _________________TIC-TAC-TOE_________________ ########

# official code for color yellow = '\033[93m' should be represented as string

color_yellow = '\033[93m'
color_green = '\033[92m'
color_red = '\033[91m'
# original color for CLI: (need to be added at the end of sting to keep the balance)

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
end = False
quit = False

# -----------------------------------------||||-------------------------------------------------


def score():
    print(color_red + " P1:" + str(player1_point) + ", P2:" + str(player2_point) + color_white)
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

def list_checker_p1():
    global x
    global player1_point
    global playtime_count

    def mess1():
        global x
        global player1_point
        global playtime_count
        renew_gui()
        player1_point += 1
        if player1_point == 3:
            x = True
        l1_p1.clear()
        l2_p1.clear()
        l3_p1.clear()
        l1_p2.clear()
        l2_p2.clear()
        l3_p2.clear()
        playtime_count = 0
    if l1_p1.count(l1_p1[-1]) == 3:
        print(  'P1 +1')
        mess1()
        score()

    elif l2_p1.count(l2_p1[-1]) == 3:
        print(  'P1 +1')
        mess1()
        score()

    elif s1.issubset(set(l3_p1)):
        print(  'P1 +1')
        mess1()
        score()

    elif s2.issubset(set(l3_p1)):
        print(  'P1 +1')
        mess1()
        score()

def list_checker_p2():
    global x
    global player2_point
    global playtime_count

    def mess2():
        global x
        global player2_point
        global playtime_count
        renew_gui()
        player2_point += 1
        if player2_point == 3:
            x = True
        l1_p1.clear()
        l2_p1.clear()
        l3_p1.clear()
        l1_p2.clear()
        l2_p2.clear()
        l3_p2.clear()
        playtime_count = 0
    if l1_p2.count(l1_p2[-1]) == 3:
        print(  'P2 +1')
        mess2()
        score()

    elif l2_p2.count(l2_p2[-1]) == 3:
        print(  'P2 +1')
        mess2()
        score()

    elif s1.issubset(set(l3_p2)):
        print(  'P2 +1')
        mess2()
        score()

    elif s2.issubset(set(l3_p2)):
        print(  'P2 +1')
        mess2()
        score()

def append_lists_p1(i):
    l1_p1.append(i[0])
    l2_p1.append(i[-1])
    l3_p1.append(i)

def append_lists_p2(i):
    l1_p2.append(i[0])
    l2_p2.append(i[-1])
    l3_p2.append(i)

def quit_function(param):
    global quit
    if param == 'quit':
        quit = True
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
print('     ' + underline + color_yellow + text_bold('TicTacToe') + color_white)
print('')
print(color_yellow + '  Whoever gets 3 point first will win the game!' + color_white)
print('')

print(color_yellow + '    GL HF!!' + color_white)



print(gui)

while x is None:
    while True:
        p1_input = input(text_bold('(P1) Row and Column number: '))
        if p1_input in gui:
            append_lists_p1(p1_input)
            playtime_count += 1
            gui = gui.replace(p1_input, color_yellow + '"X"' + color_green)
            print(gui)
            break
        elif p1_input == 'quit':
            quit_function(p1_input)
            break
        else:
            print(text_red('Row and Column ->> not valid OR already taken!'))
            continue
    if playtime_count == 9:
        end = True
        print(text_red(text_bold('It\'s a DRAW')))
        score()
        if end:
            continue
    if quit:
        break
    list_checker_p1()
    if x:
        continue
    while True:
        p2_input = input(text_bold('(P2) Row and Column number: '))
        if p2_input in gui:
            append_lists_p2(p2_input)
            playtime_count += 1
            gui = gui.replace(p2_input, color_yellow + '"O"' + color_green)
            print(gui)
            break
        elif p2_input == 'quit':
            quit_function(p2_input)
            break
        else:
            print(text_red('Row and Column ->> not valid OR already taken!'))
            continue
    if playtime_count == 9:
        end = True
        print(text_red(text_bold('It\'s a DRAW')))
        score()
    if end:
        continue
    if quit:
        break
    list_checker_p2()

if player1_point == 3:
    print("P1 WON")
elif player2_point == 3:
    print("P2 WON!")