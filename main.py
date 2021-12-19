######## _________________TIC-TAC-TOE_________________ ########


# official code for color yellow = '\033[93m' should be represented as string

color_yellow = '\033[93m'
color_green = '\033[92m'

# original color for CLI: (need to be added at the end of sting to keep the balance)

color_white = '\033[0m'

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

def list_checker_p1():
    global x
    if l1_p1.count(l1_p1[-1]) == 3:
        print('You win P1!!')
        x = True
    elif l2_p1.count(l2_p1[-1]) == 3:
        print('You win P1!!')
        x = True
    elif s1.issubset(set(l3_p1)):
        print('You win P1!!')
        x = True
    elif s2.issubset(set(l3_p1)):
        print('You win P1!!')
        x = True

def list_checker_p2():
    global x
    if l1_p2.count(l1_p2[-1]) == 3:
        print('You win P2!!')
        x = True
    elif l2_p2.count(l2_p2[-1]) == 3:
        print('You win P2!!')
        x = True
    elif s1.issubset(set(l3_p2)):
        print('You win P2!!')
        x = True
    elif s2.issubset(set(l3_p2)):
        print('You win P2!!')
        x = True

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

x = None
quit = False
print(gui)
playtime_count = 0
while x is None:
    while True:
        p1_input = input('(P1) Row and Column number: ')
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
            print('Row and Column ->> not valid OR already taken!')
            continue
    if playtime_count == 9:
        quit = True
    if quit:
        break
    list_checker_p1()
    if x is True:
        continue
    while True:
        p2_input = input('(P2) Row and Column number: ')
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
            print('Row and Column ->> not valid OR already taken!')
            continue
    if playtime_count == 9:
        quit = True
    if quit:
        break
    list_checker_p2()
