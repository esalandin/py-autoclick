import pyautogui


def printUsage():
    print('--- autoclick per FOE - assedio ---')
    print('p1 imposta posizione 1 (freccia arancione)')
    print('p2 imposta posizione 2 (paga e posiziona)')
    print('c  click')
    print('s  salva le posizioni su file')
    print('l  carica le posizioni da file')
    print('v1 vai alla posizione 1')
    print('v2 vai alla posizione 2')
    print('premendo solo enter si ripete l\'ultimo comando')
    

optfname='/tmp/autoclick-foe-options'
printUsage()

pos1=None
pos2=None

try:
    cmd=''
    while True and cmd!='quit':
        cmd = input()
        if cmd == '':
            cmd=lastcmd
        else:
            lastcmd=cmd
        if cmd == 'p1':
            pos1= pyautogui.position()
            print(pos1)
        elif cmd == 'p2':
            pos2= pyautogui.position()
            print(pos2)
        elif cmd=='v1':
            print(pos1)
            pyautogui.moveTo(pos1)
        elif cmd=='v2':
            print(pos2)
            pyautogui.moveTo(pos2)
        elif cmd=='c':
            if pos1 is None or pos2 is None:
                print('posizioni non definite')
            else:
                print("click")
                pos0= pyautogui.position()
                pyautogui.moveTo(pos1)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                pyautogui.move(5,0)
                pyautogui.move(-5,0)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                pyautogui.moveTo(pos2)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                pyautogui.moveTo(pos0)
        elif cmd=='s':
            with open(optfname, 'w') as optf:
                optf.writelines([str(pos1.x), '\n', str(pos1.y), '\n'])
                optf.writelines([str(pos2.x), '\n', str(pos2.y), '\n'])
                print(pos1)
                print(pos2)
                print('saved')
                optf.close()
        elif cmd=='l':
            pos0=pyautogui.position()
            with open(optfname) as optf:
                pyautogui.moveTo(int(optf.readline()), int(optf.readline()))
                pos1= pyautogui.position()
                pyautogui.moveTo(int(optf.readline()), int(optf.readline()))
                pos2= pyautogui.position()
                print(pos1)
                print(pos2)
                print('loaded')
                optf.close()
            pyautogui.moveTo(pos0)
        elif cmd=='h':
            printUsage()
        elif cmd=='quit':
            print("quit")
        else:
            print('comando sconosciuto')
except KeyboardInterrupt:
    print('exit\n')
