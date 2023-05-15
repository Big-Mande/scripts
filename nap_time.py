import pyautogui as mouse
from pynput import keyboard
from pynput.keyboard import Key, Controller, Listener
import time

## stop flag
staaaaaaap_haha = False

## lil function to listen to keyboard
def on_press(key):
    global staaaaaaap_haha
    if key == keyboard.Key.esc:
        print('naptime over lil bro')
        print('script ending...')
        staaaaaaap_haha = True

## set up errything for infinite l00ps
listener = keyboard.Listener(on_press=on_press)
listener.start()

print('aight its naptime!')
print('script is running...')
while not staaaaaaap_haha:
    mouse.moveRel(340, 0, 3)
    mouse.moveRel(-340, 0, 3)
        
