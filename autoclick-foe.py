import pyautogui

optfname='/tmp/autoclick-foe-options'

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
        elif cmd=='quit':
            print("quit")
        else:
            print('comando sconosciuto')
except KeyboardInterrupt:
    print('exit\n')
