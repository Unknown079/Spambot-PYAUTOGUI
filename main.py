import time
import pyautogui as pg

user = pg.prompt("Enter the amount of times..", "SPAMBOT")
x = pg.prompt("Type something: (You'll have 5 seconds time)\n", "SPAMBOT")
time.sleep(5)

for i in range(int(user)):
    ban = x
    pyautogui.write(ban)
    pyautogui.press("enter")
    
