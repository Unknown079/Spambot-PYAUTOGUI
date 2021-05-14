import time, pyautogui

#you can also configure the code if u wanna to, i made just a simple one :)
i = 0
x = [0, 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

time.sleep(5)
while True:
    pyautogui.write(str(i))
    pyautogui.press("enter")
    if i in x:
        pyautogui.write("U are gay")
        pyautogui.press("enter")
    i += 1
