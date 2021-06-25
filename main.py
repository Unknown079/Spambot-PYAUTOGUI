import time
import pyautogui

x = pyautogui.prompt("Type something: (You'll have 5 seconds time)\n", "SPAMBOT")
time.sleep(5)

while True:
    ban = x
    pyautogui.write(ban)
    pyautogui.press("enter")
    
