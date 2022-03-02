from imports import *

keyboard = Controller()

#  ======== settings ========
resume_key = Key.end
pause_key = Key.backspace
exit_key = Key.backspace
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")

def display_controls():
    print("Autofisher is running")
    print("- Controls:")
    print("\t end = Resume")
    print("\t backspace = Pause")
    print("\t backspace = Exit")
    print("-----------------------------------------------------")
    print('Press f1 to start ...')

def main():

    cast = 0

    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            if cast == 0 and pyautogui.locateOnScreen('fish.png', confidence = 0.5) != None:
                pydirectinput.keyDown('e')
                pydirectinput.keyUp('e')
                cast = 1
                print('The rod should be casted')
                time.sleep(3)
                
            if cast == 1 and pyautogui.locateOnScreen('point.png', confidence = 0.8) != None:
                print('Yeeting the fish')
                pydirectinput.keyDown('e')
                pydirectinput.keyUp('e')
                time.sleep(7)
                print('Grats (hopefully)')
                cast = 0
            else:
                print('Waiting for a bite...')
            lis.stop()

if __name__ == "__main__":
    main()
