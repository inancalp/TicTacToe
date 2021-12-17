

######## _________________TIC-TAC-TOE_________________ ########

gui = """
    -------------------------
    | (1,1) | (1,2) | (1,3) |
    -------------------------
    | (2,1) | (2,2) | (2,3) |
    -------------------------
    | (3,1) | (3,2) | (3,3) |
    -------------------------
"""

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

x = None

print(gui)

while x is None:
    while True:
        p1_input = input('(P1) Row and Column number: ')
        if p1_input in gui:
            append_lists_p1(p1_input)
            gui = gui.replace(p1_input, '"X"')
            print(gui)
            break
        else:
            print('Row and Column ->> not valid OR already taken!')
            continue
    list_checker_p1()
    if x is True:
        continue
    while True:
        p2_input = input('(P2) Row and Column number: ')
        if p2_input in gui:
            append_lists_p2(p2_input)
            gui = gui.replace(p2_input, '"O"')
            print(gui)
            break
        else:
            print('Row and Column ->> not valid OR already taken!')
            continue
    list_checker_p2()
