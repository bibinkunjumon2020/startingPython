import pyautogui as gui
import time

message=open('F://animals.txt')
message_2="Sunapy is a "
time.sleep(4)
for i in message:
    gui.typewrite(message_2+i)
    gui.press('Enter')





