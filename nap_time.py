import pyautogui as mouse
import keyboard as key
import time
print('aight its naptime!')
print('script is running...')
while(True):
    try:
        mouse.moveRel(540, 0, 3)
        mouse.moveRel(-540, 0, 3)
        time.sleep(1)
        if key.is_pressed('q'):
            print('naptime over homie')
            print('ending script...')
            break
    except Exception as e:
        print(f"oopsie an error ocurred: {e}")
        continue
