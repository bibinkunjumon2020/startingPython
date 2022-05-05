import pyautogui as gui
import time

message=input("Your Message")
number=int(input("How many messages"))
time.sleep(4)
for i in range(number):
    gui.typewrite(message)
    gui.press('Enter')
